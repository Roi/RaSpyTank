from tank import GPIO

class TankGPIO:

    def __init__(self):
        
        self.speeds = {
            'low' : 25,
            'medium' : 50,
            'high' : 75
        }

        self.actions = { 
            's'  : 'stop', 
            'f'  : 'move_forward',
            'b'  : 'move_backword',
            'fl' : 'move_forward_left', 
            'fr' : 'move_forward_right',
            'bl' : 'move_backword_left',
            'br' : 'move_backword_right',
            'l'  : 'low',
            'm'  : 'medium', 
            'h'  : 'high', 
            'e'  : 'cleanup',
            're' : 'restart'
        }

        self.inputsMapping = {
            'rb' : 12, #right_back
            'rf' : 11, #right_forward
            're' : 18, #right_engine
            'lb' : 13, #left_back
            'lf' : 15, #left_forward
            'le' : 16  #left_engine
        }

        self.directionsInputs = [ 'rf', 'lf', 'rb', 'lb' ]

        self.engineInputs = [ 're', 'le' ]

        
   
    
        

