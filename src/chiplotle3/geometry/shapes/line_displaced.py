from __future__ import division
from builtins import range
from past.utils import old_div
from chiplotle3.geometry.shapes.path_linear import path_linear
from chiplotle3.geometry.transforms.perpendicular_displace \
   import perpendicular_displace

def line_displaced(start_coord, end_coord, displacements):
   '''Returns a Path defined as a line spanning points `start_coord` and
   `end_coord`, displaced by scalars `displacements`. 
   The number of points in the path is determined by the lenght of 
   `displacements`.
   '''
   unit = old_div((end_coord - start_coord).magnitude, len(displacements))

   path = path_linear((start_coord, end_coord), unit)
   perpendicular_displace(path, displacements)
   
   return path

   
   

if __name__ == '__main__':
   from chiplotle3 import *
   import math

   disp = [math.sin(i**0.7 / 3.14159 * 2) * 100  for i in range(200)]
   line = line_displaced(Coordinate(0, 0), Coordinate(1000, 1000), disp)

   io.view(line)
