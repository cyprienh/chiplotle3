from builtins import str
from chiplotle3.hpgl.abstract.hpgl import _HPGL

class _HPGLPrimitive(_HPGL):

   _terminator = ';'


   @property
   def format(self):
      return '%s%s' % (self._name, _HPGLPrimitive._terminator)

   ### OVERRIDES ###

   ### TODO: [VA] make this simpler. remove all but the name?
   def __repr__(self):
      attributes = [ ]
      for a in dir(self):
         if not a.startswith('_'):
            if not callable(getattr(self, a)):
               #if a not in ('x', 'y', 'format', 'terminator'):
               if a not in ('x', 'y', 'format'):
                  attributes.append( '%s=%s' %(a, str(getattr(self, a))) )
      result = '%s(%s)' % (self._name, ', '.join(attributes))
      return result
