class RipplesController():
    def __init__( self, in_registrar ):
        # Inputs.
        self.registrar = in_registrar

        # Register events. Registrar::register_event( source_method : String, event_name : String )
        self.registrar.register_event( "RipplesController.configure_ripples_animation", "complete" )

        # Register receivers. Registrar::register_receiver( method_to_run : Closure, source_method : String, event_name : String )
        self.registrar.register_receiver( self.configure_ripples_animation, "RipplesView.start_animation_instruction_received", "start_animation_instruction_received" )

    def configure_ripples_animation( self ):
        # User settings.
        colors = [ "red", "blue", "green", "purple", "orange" ]     # Each circle's colour will be randomly taken from this list.
        numtrts = 100                                               # Rainfall density.
        raindrop = 1                                                # Initial ripple size.
        maxrad = 40                                                 # Maximum ripple radius.
        delay = 1                                                   # Delay between modification of turtles and screen update.
        current = 3                                                 # Speed at which turtles move along.
        run = True                                                  # Animation runs while this is true.

        # Techie settings.
        trtloc = 2                  # A modulus value for locating turtles in the array which stores the turtles and their data. Modify
                                    # this when you add or take away turtle data.
        xfrom, xto = -300, 300      # Animation area width.
        yfrom, yto = -400, 400      # Animation area height.

        # Save user settings to the registrar.
        self.registrar.save( colors, "colors" )
        self.registrar.save( numtrts, "numtrts" )
        self.registrar.save( raindrop, "raindrop" )
        self.registrar.save( maxrad, "maxrad" )
        self.registrar.save( delay, "delay" )
        self.registrar.save( current, "current" )
        self.registrar.save( run, "run" )
        self.registrar.save( trtloc, "trtloc" )
        self.registrar.save( xfrom, "xfrom" )
        self.registrar.save( xto, "xto" )
        self.registrar.save( yfrom, "yfrom" )
        self.registrar.save( yto, "yto" )

        self.registrar.notify( "RipplesController.configure_ripples_animation", "complete" )
