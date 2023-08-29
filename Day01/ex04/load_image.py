import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    try:
        image = Image.open(path)
        print(f"The format of the image is: {image.format}")
        print(f"The shape of the image is: {np.array(image).shape}")
        print("Pixel Content: ")
        print(np.array(image))
        return np.array(image)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
    return []