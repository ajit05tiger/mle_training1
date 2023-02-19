import argparse
import os
import pickle

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error

parser = argparse.ArgumentParser(description="Training")
parser.add_argument("--loc_dir", metavar="loc_dir", type=str, help="input prepared test data", default="datasets")
parser.add_argument(
    "--pickle_loc",
    metavar="pickle_loc",
    type=str,
    help="Store model pickle file",
    default="artifacts/model_pickle_files",
)
args = parser.parse_args()
loc_dir = args.loc_dir
pickle_loc = args.pickle_loc
housing_prepared = pd.read_csv(os.path.join(loc_dir, "housing_prepared.csv"))
housing_labels = pd.read_csv(os.path.join(loc_dir, "housing_labels.csv"))
X_test_prepared = pd.read_csv(os.path.join(loc_dir, "X_test_prepared.csv"))
y_test = pd.read_csv(os.path.join(loc_dir, "y_test.csv"))

pickled_model_lin_reg = pickle.load(open(os.path.join(pickle_loc, "lin_reg.pkl"), "rb"))

housing_predictions = pickled_model_lin_reg.predict(housing_prepared)
lin_mse = mean_squared_error(housing_labels, housing_predictions)
lin_rmse = np.sqrt(lin_mse)
print("root_mean_squared_error lin_reg = ", lin_rmse)

pickled_model_tree_reg = pickle.load(open(os.path.join(pickle_loc, "tree_reg.pkl"), "rb"))

housing_predictions = pickled_model_tree_reg.predict(housing_prepared)
tree_mse = mean_squared_error(housing_labels, housing_predictions)
tree_rmse = np.sqrt(tree_mse)
print("root_mean_squared_error tree_reg = ", tree_rmse)

pickled_model_final = pickle.load(open(os.path.join(pickle_loc, "final_model.pkl"), "rb"))

final_predictions = pickled_model_final.predict(X_test_prepared)
final_mse = mean_squared_error(y_test, final_predictions)
final_rmse = np.sqrt(final_mse)
print("root_mean_squared_error final_model = ", final_rmse)
