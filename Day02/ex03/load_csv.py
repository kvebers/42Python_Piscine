import csv
from typing import List


def load(path: str) -> List[List[str]]:
    try:
        with open(path, 'r') as f:
            reader = csv.reader(f)
            data = []
            for row in reader:
                data.append(row)
            print(f"Dataset dimensions: {len(data)} rows x {len(data[0])} columns")
            return data
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except csv.Error as e:
        print(f"CSV error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    except AssertionError as e:
        print(AssertionError.__name__ + ":" + str(e))
    return None