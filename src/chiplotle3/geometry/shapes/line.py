from __future__ import print_function
from chiplotle3.geometry.core.path import Path

def line(startpoint, endpoint):
   '''Returns a Path with only two points. 
   The path describes a simple straight line.
   '''
   return Path([startpoint, endpoint])


## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle3.tools import io
   
   l = line((0,0), (1000,1000))
   print(l.format)
   io.view(l)
