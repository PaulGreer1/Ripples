from turtle import *
from random import Random

class RipplesView():
    def __init__( self, in_tk, in_registrar ):
        # Inputs.
        self.tk = in_tk
        self.registrar = in_registrar

        # Register events. Registrar::register_event( source_method : String, event_name : String )
        self.registrar.register_event( "RipplesView.start_animation_instruction_received", "start_animation_instruction_received" )

        # Register receivers. Registrar::register_receiver( method_to_run : Closure, source_method : String, event_name : String )
        self.registrar.register_receiver( self.run_animation, "RipplesController.configure_ripples_animation", "complete" )

        # User interface.
        self.e1 = self.tk.Entry( getcanvas() )
        self.e1.grid( row=1, column=0 )

        b1 = self.tk.Button( getcanvas(), text='Start', command=self.start_animation_instruction_received )
        b1.grid( row=1, column=2 )

        b2 = self.tk.Button( getcanvas(), text='Stop', command=self.stop_animation_instruction_received )
        b2.grid( row=2, column=2 )

    def start_animation_instruction_received( self ):
        self.registrar.notify( "RipplesView.start_animation_instruction_received", "start_animation_instruction_received" )

    def stop_animation_instruction_received( self ):
        self.registrar.save( False, "run" )

    def run_animation( self ):
        print( self.e1.get() )
        clearscreen()
        tracer(0)             # If this is on, then every single thing that a turtle does is displayed as it happens.
        hideturtle()          # Hide the default turtle.
        #circle(50)

        # ****** INITIALIZE ****** Instantiate and position some turtles.
        r = Random()
        trts = []
        i = 0
        while i < self.registrar.get( "numtrts" ):
            trt = Turtle( visible = False )             # Create a new turtle.
            index = r.randint( 0, len( self.registrar.get("colors") ) - 1 )
            trt.fillcolor( self.registrar.get("colors")[index] )
            trt.pencolor( self.registrar.get("colors")[index] )
            trt.speed(1)
            trt.penup()
            trt.goto( r.randint( self.registrar.get("xfrom"), self.registrar.get("xto") ),
                      r.randint( self.registrar.get("yfrom"), self.registrar.get("yto") ) )      # Position the turtle somewhere.
            trts.append( trt )                                                                   # Store the turtle in the trts array.
            trts.append( r.randint( 1, self.registrar.get("maxrad") ) )                          # Radius of the turtle's initial circle.
            i = i + 1

		# Enter animation loop. 'Frames' are created, updated and displayed dynamically.
        while self.registrar.get("run"):
            # ****** CLEAR ****** Each iteration of the following loop clears a turtle's current state.
            j = 0
            while j < len( trts ):                                   # Delete the turtles' drawings and restore their default values.
                if( j % self.registrar.get("trtloc") == 0 ):
                    trts[j].clear()
                j = j + 1

            # ****** SET ****** Set turtles with data from the registrar. Each iteration of the following loop moves a turtle to its next state.
            j = 0
            while j < len( trts ):                                   # For each turtle...
                if( j % self.registrar.get("trtloc") == 0 ):
                    rad = trts[j+1]                                  # ...retrieve turtle's last recorded radius...
                    if( rad > self.registrar.get("maxrad") ):        # ...and if the turtle's radius is greater than the maximum allowed...
                        rad = self.registrar.get("raindrop")         # ...then reset the turtle's radius to raindrop size...
                        trts[j].penup()
                        trts[j].goto( r.randint( self.registrar.get("xfrom"), self.registrar.get("xto") ),
                                      r.randint( self.registrar.get("yfrom"), self.registrar.get("yto") ) )       # ...and send the turtle somewhere else.
                        trts[j].pendown()
                    rad = rad + 1                        # Increment the turtle's ripple radius.
                    trts[j].left(90)
                    trts[j].penup()
                    trts[j].forward( self.registrar.get("current") )
                    trts[j].pendown()
                    trts[j].right(90)

					# ****** SAVE ****** Save current turtle data to registrar.
                    trts[j+1] = rad                      # Replace the radius currently stored for the turtle with the new radius.
                    #trts[j].fillcolor( self.registrar.get("colors")[index] )
                    #trts[j].pencolor("#ffffff")
                    #trts[j].begin_fill()
                    trts[j].circle( rad )                # Update the turtle's ripple.
                    #trts[j].end_fill()
                j = j + 1

            # ****** DISPLAY ******
            update()                                          # Update the screen to display the updated turtles.
            ontimer( None, self.registrar.get("delay") )      # If things appear to be happening too quickly or slowly, then adjust the delay.

        return "FINISHED"
