from __future__ import division
from builtins import range
from past.utils import old_div
from chiplotle3.geometry.core.polygon import Polygon
from chiplotle3.geometry.transforms.scale import scale
import math

def circle(radius, segments = 36):
   '''Returns a circle.'''
   coords = [(math.cos(old_div(math.pi * 2, segments) * r) * radius, 
              math.sin(old_div(math.pi * 2, segments) * r) * radius) 
              for r in range(segments)]
   return Polygon(coords)


## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle3.tools import io
   e = circle(1000)
   io.view(e)
