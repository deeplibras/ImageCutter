from utils.ImageUtils import ImageUtils
from PIL import Image

"""
This class implements functions to easy manipulate images sizes.

by: Rodrigo Briet
"""
class ImageCutter(object):
    
    def cut(imageAsByte, point, height, width):
        pass
    
    """
    Cut a Pil.Image.Image from a specific point to all directions
    
    Parameters:
    <PIL.Image.Image:image>: The image to cut
    <dict:point>: The point to be the center in the cut
    <int:range>: The range to be expanded from the point to all directions
    
    Return:
    <PIL.Image.Image:cuttedImage>
    """
    def cut(image, point, range):
        # Verify the inputs types
        if(not isinstance(image, type(Image.Image()))):
            raise ValueError("Expected: "+ str(type(Image.Image())) + ". Given: "+ str(type(image)))
        if(not isinstance(point, dict)):
            raise ValueError("Expected: "+ str(type(dict())) + ". Given: "+ str(type(point)))
        if(not isinstance(range, int)):
            raise ValueError("Expected: "+ str(type(int())) + ". Given: "+ str(type(range)))
        
        # Get the image width and height
        width, height = image.size
        
        # Verify the inputs values
        if("x" not in point or "y" not in point):
            raise ValueError("The dict need to have the keys x and y")
        if(range <= 0):
            raise ValueError("range need to bigger than 0")
        if (point["x"] > width or point["y"] > height):
            raise ValueError("The coordinates not fit the original image size")
        if (range * 2 > width or range * 2 > height):
            raise ValueError("The new image size is bigger than the original image size. Original: ("+ str(width) + "," + str(height) +"). New: "+ str(range*2) + "," + str(range*2))
        
        # Cut and return the image
        return image.crop(ImageCutter.__calculateCutterArea(point, range, width, height))
    
    """
    Calculate the cut bounds
    
    Parameters:
    <dict:point>: The point to be the center in the cut
    <int:range>: The range to be expanded from the point to all directions
    <int:width>: The image width
    <int:height>: The image height
    
    Return:
    list(<int:leftBound>, <int:topBound>, <int:rightBound>, <int:bottomBound>)
    """
    def __calculateCutterArea(point, range, width, height):
        left = point["x"] - range
        right = point["x"] + range
        left, right = ImageCutter.__calculatePadding((left, right), width)
        
        top = point["y"] - range
        bottom = point["y"] + range
        top, bottom = ImageCutter.__calculatePadding((top, bottom), height)

        return (left, top, right, bottom)

    """
    Calculate the paddings between two bounds
    
    Parameters:
    <list:bound(<int:bound1>, <int:bound2>)>: The bounds to be calculate the paddings
    <int:limit>: The max bound size (Image width or Height). The min is 0
    
    Return:
    <int:bound1>, <int:bound2>
    """
    def __calculatePadding(bounds, limit):
        if (bounds[0] < 0): 
            bounds[1] += abs(bounds[0])
            bounds[0] = 0
        elif (bounds[1] > limit): 
            bounds[0] -= abs(bounds[1]-limit)
            bounds[1] = limit
            
        return bounds[0], bounds[1]
