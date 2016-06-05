from PIL import Image

"""
This class implements functions to work with images as bytes.

By: Rodrigo Briet
"""
class ImageUtils(object):
    """
    Read a imagem as byte
    
    Parameters:
    <str:path>: A valid image path
    
    Return:
    <bytes:data>
    """
    def readAsByte(path):
        file = open(path, "rb")
        data = file.read()
        return data
    
    """
    Save a image in a byte form
    
    Parameters:
    <PIL.Image.Image:image>: The image to be save
    <str:pathToSave>: The path to save the image
    """
    def saveImageAsByte(image, pathToSave):
        with open(pathToSave, "ab") as f:
            newFileByteArray = bytearray(ImageUtils.encodeImageToBytes(image))
            f.write(newFileByteArray)
    
    """
    Decode a <bytes:image> in a <PIL.Image.Image:image>
    
    Parameters:
    <bytes:imageAsByte>: The image as byte to be decode
    <int:width>: The image width
    <int:height>: The image height
    <str:colorMode>: A valid color Mode, default is "RGB"
    
    Return:
    <PIL.Image.Image:image>
    """
    def decodeBytesToImage(imageAsByte, width, height, colorMode = "RGB"):
        # Verify types
        if(not isinstance(imageAsByte, type(bytes()))):
            raise ValueError("Expected: "+ str(type(bytes())) + ". Given: "+ str(type(imageAsByte)))
        if(not isinstance(width, type(int()))):
            raise ValueError("Expected: "+ str(type(int())) + ". Given: "+ str(type(width)))
        if(not isinstance(height, type(int()))):
            raise ValueError("Expected: "+ str(type(int())) + ". Given: "+ str(type(height)))
        if(not isinstance(colorMode, type(str()))):
            raise ValueError("Expected: "+ str(type(str())) + ". Given: "+ str(type(colorMode)))
        
        # Transform to Image and return
        return Image.frombytes(colorMode, (width, height), imageAsByte)
    
    """
    Encode a image into a byte form
    
    Parameters:
    <PIL.Image.Image:image>: The image to be encode
    
    Return:
    <bytes:imageAsByte>
    """
    def encodeImageToBytes(image):
        # Verify types
        if(not isinstance(image, type(Image.Image()))):
            raise ValueError("Expected: "+ str(type(Image.Image())) + ". Given: "+ str(type(image)))
        
        # Return image as bytes
        return image.tobytes()
            