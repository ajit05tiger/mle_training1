import argparse
import os
import tarfile

import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
from six.moves import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


fetch_housing_data()


def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


housing = load_housing_data()

from sklearn.model_selection import train_test_split  # noqa

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

housing["income_cat"] = pd.cut(housing["median_income"], bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf], labels=[1, 2, 3, 4, 5])

from sklearn.model_selection import StratifiedShuffleSplit  # noqa

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

parser = argparse.ArgumentParser(description="storing trainig and testing datasets")
parser.add_argument("--loc_dir", metavar="loc_dir", type=str, help="store train and test datasets", default="datasets")
args = parser.parse_args()
loc_dir = args.loc_dir
os.makedirs(loc_dir, exist_ok=True)
train_set.to_csv(os.path.join(loc_dir, "train.csv"), index=False)
test_set.to_csv(os.path.join(loc_dir, "test.csv"), index=False)
strat_train_set.to_csv(os.path.join(loc_dir, "strat_train.csv"), index=False)
strat_test_set.to_csv(os.path.join(loc_dir, "strat_test.csv"), index=False)
