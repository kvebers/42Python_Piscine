from load_image import ft_load
from pimp_image import ft_blue, ft_red, ft_green, ft_invert, ft_grey, ft_grey_smooth
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def main():
    try:
        image = ft_load("landscape.jpeg")
        blueArray = ft_blue(image)
        greenArray = ft_green(image)
        redArray = ft_red(image)
        greyArray = ft_grey(image)
        greySmoothArray = ft_grey_smooth(image)
        invertedArray = ft_invert(image)
        GreenImage = Image.fromarray(greenArray)
        RedImage = Image.fromarray(redArray)
        GreyImage = Image.fromarray(greyArray)
        BlueImage = Image.fromarray(blueArray)
        InvertedImage = Image.fromarray(invertedArray)
        GreySmooth = Image.fromarray(greySmoothArray)
        OriginalImage = Image.fromarray(image)
        GreenImage.show()
        RedImage.show()
        GreyImage.show()
        BlueImage.show()
        OriginalImage.show()
        InvertedImage.show()
        GreySmooth.show()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))


if __name__ == "__main__":
    exit(main())
    