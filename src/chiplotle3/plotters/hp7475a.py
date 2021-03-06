"""
 *  This file is part of chiplotle3.
 *
 *  http://music.columbia.edu/cmc/chiplotle
"""

from chiplotle3.plotters.drawingplotter import _DrawingPlotter

class HP7475A(_DrawingPlotter):
   def __init__(self, ser, **kwargs):
      self.allowedHPGLCommands = tuple(['\x1b.', 'AA','AR','CA','CI','CP',
         'CS','DC','DF','DI','DP','DR','DT','EA','ER','EW','FT','IM','IN',
	      'IP','IW','LB','LT','OA','OC','OD','OE','OF','OH','OI','OO','OP',
         'OS','OW','PA','PD','PR','PS','PT','PU','RA','RO','RR','SA','SC',
         'SI','SL','SM','SP','SR','SS','TL','UC','VS','WG','XT','YT'])
      _DrawingPlotter.__init__(self, ser, **kwargs)
      self.type = "HP7475A"


