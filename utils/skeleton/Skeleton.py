"""
This class parse and save de coordinates and frame from a line of a coordinate file (Depth or Real)

by: Rodrigo Briet
"""

# External imports
import re
import ast

# Internal imports
from utils.Coords import Coords

class Skeleton(object):

    # Easy access specific node
    HEAD           = 0
    NECK           = 1
    SHOULDER_LEFT  = 2
    SHOULDER_RIGHT = 3
    ELBOW_LEFT     = 4
    ELBOW_RIGHT    = 5
    HAND_LEFT      = 6
    HAND_RIGHT     = 7
    TORSO          = 8
    HIP_LEFT       = 9
    HIP_RIGHT      = 10
    FOOT_LEFT      = 11
    FOOT_RIGHT     = 12
    
    """
    Split the frame name from de coords, then save the frame and populate the coords list
    """
    def __init__(self, coordsStringLine):
        # The frame name and his respective coords
        self.frame = None
        self.coords = []
    
        # Split the line between frame and coords
        coordsStringLine = re.split(" \[", coordsStringLine)

        # Save the frame and add a removed [ to the coord
        self.frame = coordsStringLine[0]
        coordsStringLine[1] = "["+coordsStringLine[1]
        
        self.__populateCoords(self.__generateCoordListFromString(coordsStringLine[1]))
        
    """
    Split each coord and generate a list from the string
    """
    def __generateCoordListFromString(self, coordsStringLine):
        # Split the coords
        newLine = re.sub("]\[","]\n[", coordsStringLine)

        # Split in the \n
        stringCoords = re.split("\n", newLine)

        # Transform the string coords in a valid Python list
        coords = []
        for i in range(0,15):
            coords.append(ast.literal_eval(stringCoords[i]))
        
        return coords
    
    """
    Generate a Coords object and save in the coords list
    """
    def __populateCoords(self, coordsList):
        for i in range (0,len(coordsList)):
            self.coords.append(Coords(coordsList[i][0], coordsList[i][1], coordsList[i][2]))
