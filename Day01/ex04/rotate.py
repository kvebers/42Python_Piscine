import numpy as np
from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt


def rotoate(image: Image):
    """
    Essentialy copy paste of previous excerisise except the rotation part
    """
    width, height = image.size
    if (width > height):
        cropImage = image.crop(((width - height) / 2, 0,
                                width - (width - height) / 2, height))
    else:
        cropImage = image.crop(0, (height - width) / 2, width,
                               height - (height - width) / 2)
    imageToArray = np.array(cropImage)

    transposed_image = np.empty_like(imageToArray)
    for i in range(imageToArray.shape[0]):
        for j in range(imageToArray.shape[1]):
            transposed_image[j, i, :] = imageToArray[i, j, :]
    rotImage = Image.fromarray(transposed_image)
    return rotImage


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
        print("This thing...")
        image = Image.open(path)
        grayscale_image = image.convert("L")
        grayscale_image_data = np.array(grayscale_image.getdata())
        print_usless(grayscale_image_data)
        newImage = rotoate(image)
        print(f"New shape after \"rotating\": {np.array(newImage).shape[0:2]}")
        fig, ax = plt.subplots()
        grayscale_image_1 = newImage.convert("L")
        print(f"Grayscale pixel content:\n{np.array(grayscale_image_1)}")
        ax.imshow(np.array(grayscale_image_1), cmap='gray')
        ax.set_title("Rotated and Grayed out")
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")
        grayscale_image_1.show()
        grayscale_image.show()
        plt.show()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    exit(main())
