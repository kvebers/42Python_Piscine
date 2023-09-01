import numpy as np
# [:, :, 0] = 0 this indicates if we want to select rows, colums or arrays


def ft_invert(array) -> np.ndarray:
    """
    Substractin from 255 the original value
    """
    try:
        newArray = array.copy()
        newArray[:, :, 0] = 255 - newArray[:, :, 0]
        newArray[:, :, 1] = 255 - newArray[:, :, 1]
        newArray[:, :, 2] = 255 - newArray[:, :, 2]
        return newArray
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
    except Exception as e:
        print(f"An error occurred: {e}")
    return []


def ft_red(array) -> np.ndarray:
    """
    Leaving Open only Red channel
    """
    try:
        newArray = array.copy()
        newArray[:, :, 1] = 0
        newArray[:, :, 2] = 0
        return (newArray)
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
    except Exception as e:
        print(f"An error occurred: {e}")
    return []


def ft_green(array) -> np.ndarray:
    """
    Leaving Open only Green channel
    """
    try:
        newArray = array.copy()
        newArray[:, :, 0] = 0
        newArray[:, :, 2] = 0
        return (newArray)
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
    except Exception as e:
        print(f"An error occurred: {e}")
    return []


def ft_blue(array) -> np.ndarray:
    """
    Leaving Open only Blue channel
    """
    try:
        newArray = array.copy()
        newArray[:, :, 0] = 0
        newArray[:, :, 1] = 0
        return (newArray)
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
    except Exception as e:
        print(f"An error occurred: {e}")
    return []


def ft_grey(array) -> np.ndarray:
    """
    Leaving Open only Blue channel
    """
    try:
        newArray = array.copy()
        newArray[:, :, 0] = newArray[:, :, 0] / 1 / 0.2989
        newArray[:, :, 1] = newArray[:, :, 1] / 1 / 0.5870
        newArray[:, :, 2] = newArray[:, :, 2] / 1 / 0.1140
        newArray[:, :, 0] = (newArray[0:, :, 0] + newArray[0:, :, 1]
                             + newArray[0:, :, 2]) / 3
        newArray[:, :, 1] = (newArray[0:, :, 0] + newArray[0:, :, 1]
                             + newArray[0:, :, 2]) / 3
        newArray[:, :, 2] = (newArray[0:, :, 0] + newArray[0:, :, 1]
                             + newArray[0:, :, 2]) / 3
        # newArray[:, :, 1] = newArray[:, :, 0]
        # newArray[:, :, 2] = newArray[:, :, 0]
        return (newArray)
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
    except Exception as e:
        print(f"An error occurred: {e}")
    return []
