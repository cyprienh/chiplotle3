from chiplotle3.core.cfg.cfg import __version__
from chiplotle3.core.cfg.initialize_files import initialize_files
__authors__ = "Victor Adan, Douglas Repetto"
__license__ = "GPL"
__url__     = "http://music.columbia.edu/cmc/chiplotle"
__doc__     = \
"""Chiplotle
Python library for pen plotting.

Copyright %s
Version %s
License %s
Homepage %s

""" % (__authors__,__version__,__license__,__url__)

initialize_files()
globals().pop('initialize_files')


## IMPORTS ##

from chiplotle3.core import errors

from chiplotle3.geometry.core.coordinatearray import CoordinateArray
from chiplotle3.geometry.core.coordinate import Coordinate

from chiplotle3.hpgl import commands as hpgl
from chiplotle3.hpgl import formatters
from chiplotle3.hpgl.pen import Pen

from chiplotle3.geometry.core import Group
from chiplotle3.geometry.core import Path
from chiplotle3.geometry.core import Polygon
from chiplotle3.geometry.core import Label
from chiplotle3.geometry import shapes
from chiplotle3.geometry import transforms
from chiplotle3.geometry.shapes import *
from chiplotle3.geometry.transforms import *

from chiplotle3.tools.plottertools import instantiate_plotters
from chiplotle3.tools.plottertools import instantiate_virtual_plotter
from chiplotle3.tools import *

from chiplotle3 import plotters


## shortcuts / abbreviations ##

CoordArray = CoordinateArray
Coord = Coordinate

## remove unnecessary modules...
#globals().pop('hpgl')
#globals().pop('tools')
#globals().pop('utils')
