import pandas as pd


def load(path: str) -> pd.DataFrame:
    try:
        data = pd.read_csv(path)
        print(f"Dataset dimensions: {data.shape[0]} rows x {data.shape[1]} columns")
        return data
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: File '{path}' is empty.")
    except pd.errors.ParserError as e:
        print(f"CSV parsing error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None