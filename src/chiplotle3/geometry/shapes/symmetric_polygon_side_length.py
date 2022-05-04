from __future__ import division
from past.utils import old_div
from chiplotle3.geometry.shapes.circle import circle
from chiplotle3.geometry.transforms.scale import scale

def symmetric_polygon_side_length(count, length):
   '''Creates a symmetric polygon with `count` sides, all with the 
   same given `length`.
   '''
   result = circle(1.0, count)
   scale(result, old_div(length, result.points.difference[0].magnitude))
   return result
