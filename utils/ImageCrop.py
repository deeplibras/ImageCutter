"""
This file implements a function to crop a image from a point in all directions
keeping a determined ratio from the new border to the point.
If the ratio is out of bound from the original image a padding is added to the 
opposite side to keep the wanted proportion (width , height).

by: Rodrigo Briet
"""

# External imports
from PIL import Image
from os import path

"""
Crop a image from a point(X, Y) keeping a size to all directions
"""
def crop(coordX, coordY, ratio, image):
    
    # Verify parameters
    if(not isinstance(coordX, int)):
        raise ValueError("coordX must be a integer")
    if(not isinstance(coordY, int)):
        raise ValueError("coordY must be a integer")
    if(not isinstance(ratio, int)):
        raise ValueError("coordX must be a integer")
    #if(not isinstance(image, type(Image))):
    #    raise ValueError("image must be a PIL.Image.Image type")
    
    # Get original image size
    width, height = image.size
    
    # Verify coords location and ratio size
    if (coordX > width or coordY > height):
        raise ValueError("The coordinates not fit the original image size")

    if (ratio * 2 > width or ratio * 2 > height):
        raise ValueError("The new image size is bigger than the original image size")
        
    # Crop and return the new image
    return image.crop(__calculateCropArea(coordX, coordY, ratio, width, height))

"""
Calculate the crop area from original image
"""
def __calculateCropArea(coordX, coordY, ratio, width, height):
    # Define the crop area LEFT - RIGHT
    left = coordX - ratio
    right = coordX + ratio
    left, right = __calculatePadding(left, right, width)
    
    # Define the crop area TOP - BOTTOM
    top = coordY - ratio
    bottom = coordY + ratio
    top, bottom = __calculatePadding(top, bottom, height)

    return (left, top, right, bottom)

"""
Calculate the padding need to keep the wanted ratio
If point1 is out of bounds (0), add a padding to point2
If point2 is out of bounds (limit), add a padding to point1
"""
def __calculatePadding(point1, point2, limit):
    if (point1 < 0): 
        point2 += abs(point1)
        point1 = 0
    elif (point2 > limit): 
        point1 -= abs(point2-limit)
        point2 = limit
        
    return point1, point2