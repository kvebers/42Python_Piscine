from load_image import ft_load
from pimp_image import ft_blue, ft_red, ft_green, ft_invert, ft_grey
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def main():
    try:
        image = ft_load("landscape.jpeg")
        blueArray = ft_blue(image)
        greenArray = ft_green(image)
        redArray = ft_green(image)
        greyArray = ft_grey(image)
        invertedArray = ft_invert(image)
        GreenImage = Image.fromarray(rotated_image)
        RedImage = Image.fromarray(rotated_image)
        GreyImage = Image.fromarray(rotated_image)
        BlueImage = Image.fromarray(rotated_image)
        InvertedImage = Image.fromarray(rotated_image)
        OriginalImage = Image.fromarray(image)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))

        
if __name__ == "__main__":
    exit(main())
    