from load_image import ft_load
from pimp_image import ft_blue, ft_red, ft_green
from pimp_image import ft_invert, ft_grey
from PIL import Image


def main():
    try:
        image = ft_load("landscape.jpeg")
        blueArray = ft_blue(image)
        greenArray = ft_green(image)
        redArray = ft_red(image)
        greyArray = ft_grey(image)
        invertedArray = ft_invert(image)

        GreenImage = Image.fromarray(greenArray)
        RedImage = Image.fromarray(redArray)
        GreyImage = Image.fromarray(greyArray)
        BlueImage = Image.fromarray(blueArray)
        InvertedImage = Image.fromarray(invertedArray)
        OriginalImage = Image.fromarray(image)

        GreenImage.show()
        RedImage.show()
        GreyImage.show()
        BlueImage.show()
        OriginalImage.show()
        InvertedImage.show()
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    exit(main())
