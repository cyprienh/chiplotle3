from __future__ import print_function
#from chiplotle3.geometry.core.path import Path
from chiplotle3.geometry.core.polygon import Polygon

def isosceles(width, height, filled=False):

   tip = (0, height)
   left = (- width / 2.0, 0)
   right = (width / 2.0, 0)

   return Polygon([tip, left, right, tip], filled = filled)



## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle3.tools import io
   e = isosceles(200, 400, filled=True)
   print(e.format)
   io.view(e)
