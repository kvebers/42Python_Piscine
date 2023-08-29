import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

"""
[:, :, 0] = 0 this indicates if we want to select rows, colums or arrays
"""

"""
Substractin from 255 the original value
"""

def ft_grey_smooth(array) ->np.ndarray:
    try:
        newArray = array.copy()
        newArray[:, :, 0] = newArray[:, :, 0] * 0.2989
        newArray[:, :, 1] = newArray[:, :, 1] * 0.5870
        newArray[:, :, 2] = newArray[:, :, 2] * 0.1140
        return ft_grey(newArray)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
    return []

def ft_invert(array) -> np.ndarray:
    try:
        newArray = array.copy()
        newArray[:, :, 0] = 255 - newArray[:, :, 0]
        newArray[:, :, 1] = 255 - newArray[:, :, 1]
        newArray[:, :, 2] = 255 - newArray[:, :, 2]
        return newArray
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
    return []


"""
Leaving Open only Red channel
"""
def ft_red(array) -> np.ndarray:
    try:
        newArray = array.copy()
        newArray[:, :, 1] = 0
        newArray[:, :, 2] = 0
        return (newArray)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
    return []

"""
Leaving Open only Green channel
"""

def ft_green(array) -> np.ndarray:
    try:
        newArray = array.copy()
        newArray[:, :, 0] = 0
        newArray[:, :, 2] = 0
        return (newArray)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
    return []



"""
Leaving Open only Blue channel
"""
def ft_blue(array) -> np.ndarray:
    try:
        newArray = array.copy()
        newArray[:, :, 0] = 0
        newArray[:, :, 1] = 0
        return (newArray)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
    return []

"""
Leaving Open only Blue channel
"""

def ft_grey(array) -> np.ndarray:
    try:
        newArray = array.copy()
        newArray[:, :, 0] = (array[0:, :, 0] + array[0:, :, 1] + array[0:, :, 2]) / 3
        newArray[:, :, 1] = (array[0:, :, 0] + array[0:, :, 1] + array[0:, :, 2]) / 3 
        newArray[:, :, 2] = (array[0:, :, 0] + array[0:, :, 1] + array[0:, :, 2]) / 3 
        return (newArray)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
    return []

    