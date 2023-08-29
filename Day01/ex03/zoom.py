import numpy as np
from PIL import Image, ImageDraw, ImageFont
from load_image import ft_load
import matplotlib.pyplot as plt

"""
MY OWN FANCY ZOOM FUNCTION XD
"""
def zoom_image(image: Image):
    width, height = image.size
    zoomed_image = image.crop((width / 4, height / 4, width / 4 * 3, height / 4 * 3))
    scaled_image = zoomed_image.resize((2 * zoomed_image.width, 2 * zoomed_image.height))
    
    return scaled_image

def main():
    try:
        """
        DEFINES THE PATH OF THE IMAGE AND PRINTS OUT STUFF
        """
        path = "animal.jpeg"
        ft_load(path)
        image = Image.open(path)
        newImage = zoom_image(image)
        print(f"New shape after \"zooming\": {np.array(newImage).shape}")
        fig, ax = plt.subplots()
        ax.imshow(np.array(newImage))
        """
        DISPLAYS THE IMAGES, NEEDED TO USE PLT because Python is awesome
        """
        ax.set_title("Zoomed and Scaled Image")
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")
        """
        I honestly do not know what they are asking here to print, but supposedly that is this
        """
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
    
