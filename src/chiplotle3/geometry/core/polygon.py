from __future__ import print_function
from chiplotle3.hpgl.commands import PM, EP, FP, FT, SP
from chiplotle3.geometry.core.coordinatearray import CoordinateArray
from chiplotle3.geometry.core.path import Path
from chiplotle3.tools.hpgltools.convert_coordinates_to_hpgl_absolute_path \
   import convert_coordinates_to_hpgl_absolute_path

class Polygon(Path):
   '''A closed path.'''

   def __init__(self, points, filled=False):  
      Path.__init__(self, points)
      self.filled = filled

   @property
   def _preformat_points(self):
      '''Points (coordinates) ready for formatting (conversion to HPGL).'''
      coords = self.points[:]
      coords.append(coords[0])
      return CoordinateArray(coords)




if __name__ == '__main__':
   from chiplotle3 import io

   p = Polygon([(0, 0), (2000, 0), (1000, 1000), (0, 500)], 0)
   print(p.points)
   print(p._preformat_points)

   io.view(p)
