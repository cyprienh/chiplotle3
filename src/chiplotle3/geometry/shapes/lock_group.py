from __future__ import division
from past.utils import old_div
from chiplotle3.geometry.core.transformlock import TransformLock
from chiplotle3.geometry.core.shape import _Shape

def lock_group(shapes, lock_transforms):
   t = TransformLock(shapes, lock_transforms)
   return t


## ~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
   from chiplotle3.geometry.shapes.square import square
   from chiplotle3.geometry.core.group import Group
   from chiplotle3.geometry.transforms.rotate import rotate
   from chiplotle3.geometry.transforms.offset import offset
   from chiplotle3 import io
   import math

   r1 = square(100)
   r2 = square(150)
   l = lock_group([r2], ['rotate'])
   g  = Group([r1, l])
   offset(g, (200, 0))
   rotate(g, old_div(math.pi, 4))
   io.view(g) 
