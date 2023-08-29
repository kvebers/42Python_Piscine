import numpy as np
from PIL import Image, ImageDraw, ImageFont
from load_image import ft_load
import matplotlib.pyplot as plt

"""
Essentialy copy paste of previous excerisise except the rotation part
"""

def rotoate(image : Image):
    width, height = image.size
    if (width > height):
        cropImage = image.crop(((width - height) / 2, 0, width - (width - height) / 2, height))
    else:
        cropImage = image.crop(0, (height - width) / 2, width, height - (height - width) / 2)
    rotImage = cropImage.rotate(-90, expand=True)
    return rotImage
    



def main():
    try:
        """
        DEFINES THE PATH OF THE IMAGE AND PRINTS OUT STUFF
        """
        path = "animal.jpeg"
        ft_load(path)
        """
        DON'T know how to display it in that format, but I made it work somehow
        """
        print("This thing...")
        image = Image.open(path)
        grayscale_image = image.convert("L")
        grayscale_image_data = np.array(grayscale_image.getdata())
        for pixel_value in grayscale_image_data[:3]:
            print(f"[{pixel_value}]")
        print(" ... ")
        for pixel_value in grayscale_image_data[-3:]:
            print(f"[{pixel_value}]")
        newImage = rotoate(image)
        print(f"New shape after \"rotating\": {np.array(newImage).shape}")
        fig, ax = plt.subplots()
        ax.imshow(np.array(newImage))
        """
        DISPLAYS THE IMAGES, NEEDED TO USE PLT because Python is awesome
        """
        ax.set_title("Zoomed and Scaled Image")
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")
        grayscale_image = newImage.convert("L")
        print(f"Grayscale pixel content:\n{np.array(grayscale_image)}")
        newImage.show()
        image.show()
        plt.show()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))


if __name__ == "__main__":
    exit(main())
    