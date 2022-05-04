from __future__ import division
from past.utils import old_div
from chiplotle3.geometry.core.coordinate import Coordinate
from chiplotle3.tools.hpgltools.get_all_coordinates import get_all_coordinates

def get_centroid(arg):
   '''Returns the centroid of the given Chiplotle-HPGL shapes.'''
   arg = get_all_coordinates(arg)
   ## convert into a set to remove duplicate coordinates and to 
   ## avoid giving more weight to these duplicate points...
   arg = set(arg)
   result = Coordinate(0, 0)
   for c in arg:
      result += c
   return old_div(result, len(arg))
      
      
