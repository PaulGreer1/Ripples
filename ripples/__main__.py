'''
Run the app by entering the following command at your command line:
python __main__.py

'''

import Tkinter as tk

# The Registrar.
from registrar import Registrar

# Views.
from ripplesview import RipplesView

# Controllers.
from ripplescontroller import RipplesController

def Main():
    """Docstring."""
    registrar = Registrar()
    view = RipplesView( tk, registrar )
    controller = RipplesController( registrar )

if( __name__ == '__main__' ):
    Main()
    tk.mainloop()
