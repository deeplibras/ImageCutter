usage = "Usage: python libLibrasImageCutter.py <str:recordFolder> <int:ratio: <str:sklPoint> [<boolean:saveOriginalImage <str:saveFolder>]"
"""
Crop all recorded frames from a libLibras (https://github.com/matheus-silva/libLibras) record folder
keeping a specific ratio from a skeleton coord point

by: Rodrigo Briet
"""
# External imports
from PIL import Image
import os
import sys
import re

# Internal imports
from utils.Skeleton import Skeleton
from utils.ImageCrop import crop
from utils.ImageLoad import loadImageFromBin

"""
Required Parameters
"""
# Verify parameters numbers
if(len(sys.argv) < 4):
    print("Invalid numbers of parameters\n"+usage)
    sys.exit()
    
# Ge the inputPath
inputPath = sys.argv[1]

# Verify the ratio input
ratio = None
if(re.match("^[\d]+$", sys.argv[2])):
    ratio = int(sys.argv[2])
    if(ratio <= 0):
        sys.exit("ratio("+sys.argv[2]+") need to be > 0")
else:
    sys.exit("ratio("+sys.argv[2]+") need to be a integer")
    
# Verify the skeleton point
skeletonPoints = {"HEAD":0, "NECK":1, "SHOULDER_LEFT":2, "SHOULDER_RIGHT":3, "ELBOW_LEFT":4, "ELBOW_RIGHT":5, 
                    "HAND_LEFT":6, "HAND_RIGHT":7, "TORSO":8, "HIP_LEFT":9, "HIP_RIGHT":10, "FOOT_LEFT":11, "FOOT_RIGHT":12}
sklPoint = None
if(sys.argv[3] not in skeletonPoints):
    print("The given sklPoint("+sys.argv[3]+") is not a valid point\nValids point are: ")
    for point in skeletonPoints:
        print(point)
    sys.exit()
else:
    sklPoint = skeletonPoints[sys.argv[3]]

"""
Optional Parameters
"""
# Get the saveOriginal
saveOriginal = False
if(len(sys.argv) == 5):
    if(sys.argv[4].lower() == "true"):
        saveOriginal = True
    elif(sys.argv[4].lower() == "false"):
        saveOriginal = False
    else:
        sys.exit("saveOriginal("+sys.argv[4]+") parameter need to be \"true\" or \"false\"")
        
# Get the saveFolder
if(len(sys.argv) >= 6):
    saveFolder = sys.argv[5]
else:
    saveFolder = inputPath+"\croppedImage"

"""
Process the images
"""
# Get the skeleton file
skeletonPath = inputPath+"\Coordinates\Depth.txt"
skeletonFile = open(skeletonPath)

# Get the skeleton to each frame in the file
skls = []
for line in skeletonFile:
    skls.append(Skeleton(line))

# Get the name of all colored images (The Color image have a diferent name from frame)
colorImagensBin = os.listdir(inputPath+"\Color\\")

# Create the folder to keep the croppedImage
if not os.path.exists(saveFolder):
    os.makedirs(saveFolder)
    
# Create the folder to keep the croppedImage
if not os.path.exists(saveFolder+"\original") and saveOriginal:
    os.makedirs(saveFolder+"\original")

# For each image crop in around the skeleton HEAD
for i in range(0, len(colorImagensBin)):
    # Load the imagem from original .bin
    image = loadImageFromBin(inputPath+"\Color\\"+colorImagensBin[i], "RGB", 640, 480)
    
    # Save the original
    if(saveOriginal):
        print("Saving original: "+skls[i].frame+".bmp")
        image.save(saveFolder+"\original\\"+skls[i].frame+".bmp")
        
    # Prepare the coords points
    x = int(round(skls[i].coords[sklPoint].X))
    y = int(round(skls[i].coords[sklPoint].Y))
    
    # Crop and save the image
    print("Cropping: " + colorImagensBin[i])
    croppedImage = crop(x, y, ratio, image)            
    print("Saving: "+saveFolder+"\\"+skls[i].frame+".bmp")
    croppedImage.save(saveFolder+"\\"+skls[i].frame+".bmp")