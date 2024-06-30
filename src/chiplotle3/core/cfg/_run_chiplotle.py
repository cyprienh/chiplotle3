from chiplotle3.core.cfg.cfg import __version__
from chiplotle3 import *

def main():
    import code
    import sys

    plts = instantiate_plotters()
    plotter = plts[0]

    banner = f"""
    +-----------------------+
    |   Chiplotle! v{__version__}  |
    +-----------------------+
    """

    sys.ps1 = "chiplotle3>"

    code.interact(banner=banner, local=globals(), exitmsg="Exiting Chiplotle3, goodbye!")

if __name__ == "__main__":
    main()
