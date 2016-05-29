"""
This file implements a function to load a image saved as bytes values

by: Rodrigo Briet
"""

# External imports
from PIL import Image

def loadImageFromBin(filename, colorMode, width, height):
    # Open and read the .bin file
    file = open(filename, "rb")
    data = file.read()
    
    # Transform the read bytes in a Image
    image = Image.frombytes(colorMode, (width, height), data)
    
    # Return the image as PIL.Image.Image
    return image