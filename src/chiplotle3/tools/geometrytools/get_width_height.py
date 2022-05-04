from chiplotle3.geometry.core.coordinate import Coordinate
from chiplotle3.geometry.core.coordinatearray import CoordinateArray
from chiplotle3.tools.geometrytools.get_minmax_coordinates import get_minmax_coordinates

def get_width_height(coords):
   '''Returns the width and height of the given `coords` list in a tuple.'''
   
   min_max = get_minmax_coordinates(coords.points)
   
   width = min_max[1][0] - min_max[0][0]
   height = min_max[1][1] - min_max[0][1]
   return (width, height)


## DEMO
if __name__ == '__main__':
   from chiplotle3.geometry.shapes.circle import circle
   from chiplotle3.geometry.shapes.random_walk_polar import random_walk_polar
   from chiplotle3.geometry.core.group import Group
   from chiplotle3.geometry.core.path import Path
   from chiplotle3.tools import io

   #random points inside a circle
   rw = random_walk_polar(100)

   assert isinstance(rw, Path)
   
   (width, height) = get_width_height(rw)
   
   #a circle around all the points
   c = circle(width/2.0, 500)
   
   g = Group((rw, c))
   
   io.view(g)
