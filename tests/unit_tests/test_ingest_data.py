import os

import pandas as pd
import pytest
from nonstandardcode import load_housing_data


def test_load_housing_data():
    assert load_housing_data() == pd.read_csv("../../datasets/housing/housing.csv")
