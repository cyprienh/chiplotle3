from chiplotle3.geometry.transforms.offset import offset
from chiplotle3.geometry.core.coordinate import Coordinate

def center_at(shape, coord):
   '''Centers shape at the given coordinate.'''
   offset(shape, -shape.center + Coordinate(*coord))
   
