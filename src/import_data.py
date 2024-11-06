import pandas as pd
import numpy as np
import os
import sys
from datetime import datetime

def import_data(file_path):
    # Reads data in the pkl format
    data = pd.read_pickle(file_path)
    return data

if __name__ == '__main__':
    # Get the file path
    file_path = '../dataset/smart_app_data.pkl'
    data = import_data(file_path)
    #print(data.head())

    # Describe the data
    print(data.describe())

    # Check the data types
    print(data.dtypes)

    # Check the missing values
    print(data.isnull().sum())