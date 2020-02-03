import pandas as pd
import matplotlib
import numpy as np
MARKETING_DATA_PATH = "bank_data_prediction_task.csv"


# Open the dataset
def load_marketing_data(csv_path):
    print("Loading the data in progress...")
    data = pd.read_csv(csv_path)
    print("Data loaded successfully.")
    return data


if __name__ == '__main__':
    # Load data from the directory
    marketing_data = load_marketing_data(MARKETING_DATA_PATH)

    # Preview
    print(marketing_data.head())

    # metadata info
    print(marketing_data.info())