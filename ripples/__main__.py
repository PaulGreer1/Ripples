'''
cd /home/dmortimer/.local/lib/python3.6/site-packages/topspek/turtlebots/ripples
python3.6 __main__.py
python __main__.py

'''

import Tkinter as tk

# The Registrar.
#from models.registrar.registrar import Registrar
from registrar import Registrar

# Views.
#from topspek.turtlebots.ripples.ripplesview import RipplesView
from ripplesview import RipplesView

# Controllers.
#from topspek.turtlebots.ripples.ripplescontroller import RipplesController
from ripplescontroller import RipplesController

def Main():
    """Docstring."""
    registrar = Registrar()
    view = RipplesView( tk, registrar )
    controller = RipplesController( registrar )

if( __name__ == '__main__'):
    Main()
    tk.mainloop()
