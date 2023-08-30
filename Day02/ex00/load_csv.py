import csv
from typing import List
import pandas as pd


def load(path: str) -> pd.DataFrame:
    try:
        with open(path, 'r') as f:
            reader = csv.reader(f)
            data = []
            for row in reader:
                data.append(row)
            print(f"Dataset dimensions: {len(data)} rows x {len(data[0])} columns")
            dataPrint = pd.read_csv(path)
            return dataPrint
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except csv.Error as e:
        print(f"CSV error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    except AssertionError as e:
        print(AssertionError.__name__ + ":" + str(e))
    return None