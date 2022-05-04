from chiplotle3.tools.geometrytools.get_minmax_coordinates \
   import get_minmax_coordinates

def get_bounding_rectangle(shape):
   '''Return a bounding box shape (rectangle) enclosing the givne `shape`.'''
   ## TODO figure out why these cause circular imports (ImportError):
   from chiplotle3.geometry.shapes.rectangle import rectangle
   from chiplotle3.geometry.transforms.offset import offset

   ll, ur = get_minmax_coordinates(shape.points)

   w, h = ur - ll
   center_x = ll.x + w / 2.0
   center_y = ll.y + h / 2.0
   
   r =  rectangle(w, h)
   offset(r, (center_x, center_y))
   return r



## DEMO CODE ##
if __name__ == '__main__':
   from chiplotle3.geometry.transforms.offset import offset
   from chiplotle3.geometry.shapes.circle import circle
   from chiplotle3.geometry.transforms.noise import noise
   from chiplotle3.geometry.core.group import Group
   from chiplotle3.tools import io

   c = circle(1000)
   offset(c, (100, 500))
   noise(c, 500)
   bb = get_bounding_rectangle(c)
   
   io.view(Group([bb, c]))

