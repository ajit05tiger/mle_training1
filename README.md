# Median housing value prediction

The housing data can be downloaded from https://raw.githubusercontent.com/ageron/handson-ml/master/. The script has codes to download the data. We have modelled the median house value on given housing data. 

The following techniques have been used: 

 - Linear regression
 - Decision Tree
 - Random Forest

## Steps performed
 - We prepare and clean the data. We check and impute for missing values.
 - Features are generated and the variables are checked for correlation.
 - Multiple sampling techinuqies are evaluated. The data set is split into train and test.
 - All the above said modelling techniques are tried and evaluated. The final metric used to evaluate is mean squared error.

## To excute the script
python < scriptname.py >

## Command to create conda environment from env.yml file
conda env create --file env.yml

## command to see created environment
conda env list

## command to activate created environment
conda activate mle-dev

## command to run python script
python nonstandardcode.py

## python packaging setup.py
from setuptools import setup

setup(
    name="py_packages",
    version="0.1",
    description="This is code for predicting house price",
    author="ajit05tiger",
    install_requires=[],
)

## creating py_packges wheel file
python setup.py sdist bdist_wheel

## importing py_packages
import py_packages
import py_packages.ingest_data

## ML-workflow scripts(ingest_data.py, train.py, score.py) with using argparse arguments
--loc_dir  as  ../../datasets
--pickled_loc  as  ../../artifacts/model_pickle_files

## making and reading pickle files
pickle.dump(final_model, open(os.path.join(pickle_loc, "final_model.pkl"), "wb"))
pickled_model_final = pickle.load(open(os.path.join(pickle_loc, "final_model.pkl"), "rb"))

## adding unit_test
test_ingest_data.py

## used sphinx to generate html documents
conda install sphinx
mkdir docs
cd docs
sphinx-quickstart
make html