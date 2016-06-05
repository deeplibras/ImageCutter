"""
This class save the X, Y and Z coords from a skeleton point

by: Rodrigo Briet
"""
class Coords(object):
    
    X = None
    Y = None
    Z = None
    
    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z