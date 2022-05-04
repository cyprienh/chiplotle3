#import serial

from builtins import range
def scan_serial_ports_windows( ):
   from chiplotle3.tools.serialtools import scan_serial_ports_from_list
   return scan_serial_ports_from_list(list(range(256)))
#   result = { }
#   ## keep track of previously opened ports to avoid including aliases
#   ## in our list...
#   ports_opened = [ ]
#   for i in range(256):
#      try:
#         s = serial.Serial(i)
#         ports_opened.append(s)
#         result[i] = s.portstr
#         #result[i] = s
#         #s.close( )   # explicit close 'cause of delayed GC in java
#      except serial.SerialException:
#         pass
#   ## gracefully close all open ports...
#   for port in ports_opened:
#      port.close( )
#   return result
   
