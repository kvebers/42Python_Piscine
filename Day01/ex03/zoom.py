import numpy as np
from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt


def zoom_image(image: Image):
    """
    MY OWN FANCY ZOOM FUNCTION XD
    """
    width, height = image.size
    zoomed_image = image.crop((width / 4, height / 4,
                               width / 4 * 3, height / 4 * 3))
    scaled_image = zoomed_image.resize((2 * zoomed_image.width,
                                        2 * zoomed_image.height))
    return scaled_image


def print_usless(grayscale_image_data):
    """PRINTS OUT THE USLESS DATA"""
    print("[[", end='')
    for pixel_value in grayscale_image_data[:3]:
        print(f"[{pixel_value}]")
    print("...")
    for pixel_value in grayscale_image_data[-3:-1]:
        print(f"[{pixel_value}]")
    print(f"[{grayscale_image_data[-1]}]]]")


def main():
    try:
        """
        DEFINES THE PATH OF THE IMAGE AND PRINTS OUT STUFF
        """
        path = "animal.jpeg"
        ft_load(path)
        image = Image.open(path)
        newImage = zoom_image(image)
        print(f"New shape after \"zooming\": {np.array(newImage).shape[0:2]}")
        grayscale_image = newImage.convert("L")
        grayscale_image_data = np.array(grayscale_image.getdata())
        print_usless(grayscale_image_data)
        fig, ax = plt.subplots()
        ax.imshow(np.array(grayscale_image), cmap='gray')
        ax.set_title("Zoomed and Scaled Image")
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")
        grayscale_image.show()
        image.show()
        plt.show()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    exit(main())
