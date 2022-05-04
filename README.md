# Chiplotle
Chiplotle is a Python library that implements and extends the HPGL (Hewlett-Packard Graphics Language) plotter control language. It supports all the standard HPGL commands as well as our own more complex "compound HPGL" commands, implemented as Python classes. Chiplotle also provides direct control of your HPGL-aware hardware via a standard usb<->serial port interface.

Chiplotle has been tested with a variety of HPGL devices from various companies, including Hewlett-Packard, Roland Digital Group, Houston Instrument, etc. It includes plotter-specific configuration files for many different plotter models, as well as a generic configuration that should work with any HPGL-compliant device. 

Chiplotle is written and maintained by Victor Adan and Douglas Repetto.

Chiplotle has been updated to Python 3 by Cyprien Heusse. 
This updated version has been tested on several different computers and operating systems (MacOS Intel & M1, Linux Mint & Raspbian, Windows).
Some information depending on the OS you install this library on:
- On Linux you will probably need to add yourself to the "dialout" group, to do so simply type `sudo usermod -a -G dialout user`.
- On MacOS using M1 processor, you might need to reinstall Numpy for the library to work, to do so `pip uninstall numpy` and `pip install numpy`.

Find all there is to know about Chiplotle at:
http://music.columbia.edu/cmc/chiplotle

The code for this version of Chiplotle is available at:
https://github.com/cyprienh/chiplotle3
