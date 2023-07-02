class Registrar():
    """
    implements event registration and callback...

    receivers is an array of arrays of sets: [ receiver, [ source, { event, ... } ... ], ... ]...
    """
    #===================================================
    def __init__( self ):
        self.events = []                #
        self.receivers = []             #
        self.data_store = dict()        #
    #===================================================
    def save( self, data, data_key ):
        self.data_store[data_key] = data
    #===================================================
    def get( self, data_key ):
        return self.data_store[data_key]
    #===================================================
    def register_event( self, source, event ):
        found = False
        i = 0
        while i < len( self.events ):
            if( (i % 2) == 0 ):
                if( self.events[i] == source ):
                    self.events[i+1].add( event )
                    found = True
                    break
            i = i + 1

        if( not found ):
            self.events.append( source )
            self.events.append( { event } )
    #===================================================
    def register_receiver( self, receiver, source, event ):
        receiver_found = False
        source_found = False
        i = 0
        while i < len( self.receivers ):
            if( (i % 2) == 0 ):
                if( self.receivers[i] == receiver ):
                    receiver_found = True
                    j = 0
                    while j < len( self.receivers[i+1] ):                   # self.receivers[i+1] is the array of event sources which this receiver is interested in...
                        if( (j % 2) == 0 ):
                            if( self.receivers[i+1][j] == source ):         # self.receivers[i+1][j] is an event source...
                                source_found = True
                                self.receivers[i+1][j+1].add( event )       # self.receivers[i+1][j+1] is the set of events for this event source...
                        j = j + 1
                    if( not source_found ):                                 # if the event source is not present for this receiver, then enter it and leave the loop...
                        self.receivers[i+1].append( source )
                        self.receivers[i+1].append( { event } )
                        break
            i = i + 1

        # if the receiver has not yet been entered, then enter the receiver along with the event source and the event for which the receiver is registering...
        if( not receiver_found ):
            self.receivers.append( receiver )
            self.receivers.append( [ source, { event } ] )
    #===================================================
    def notify( self, event_source, event_name ):
        """
        Call receiver methods which have registered for event notifications.

        """
        i = 0
        while i < len( self.receivers ):
            if( (i % 2) == 0 ):
                j = 0
                while j < len( self.receivers[i+1] ):
                    if( (j % 2) == 0 ):
                        if( self.receivers[i+1][j] == event_source ):
                            if( event_name in self.receivers[i+1][j+1] ):
                                self.receivers[i]()
                    j = j + 1
            i = i + 1
    #===================================================
