from robot import GPIO 
from robot import TankGPIO

class TankMove(TankGPIO):
    def __init__(self):
        TankGPIO.__init__(self)
        self.inputs_to_activate = []
        self.init_gpio()
        self.rep = GPIO.PWM(self.inputsMapping['re'], 1000) #right_engine pwm
        self.lep = GPIO.PWM(self.inputsMapping['le'], 1000) #left_engine pwm
        self.rep.start(50)
        self.lep.start(50)

    def init_gpio(self):    
        GPIO.setmode(GPIO.BOARD)
        #GPIO.setwarnings(False)
        
        for IM in self.inputsMapping:
            GPIO.setup(self.inputsMapping[IM], GPIO.OUT)

        for DI in self.directionsInputs:
            GPIO.output(self.inputsMapping[DI], GPIO.LOW)


    def is_channel_in_use(self,channel):
        return GPIO.input(channel)

    def set_active_state(self):
        for inp in self.directionsInputs:
            if inp in self.inputs_to_activate:
                GPIO.output(self.inputsMapping[inp], GPIO.HIGH)
            else:
                GPIO.output(self.inputsMapping[inp], GPIO.LOW)
         
    def move_forward(self):
        self.inputs_to_activate = ['rf','lf']
        self.set_active_state()
    
    def move_backword(self):
        self.inputs_to_activate = ['rb','lb']
        self.set_active_state()

    def move_forward_left(self):
        self.inputs_to_activate = ['rf']
        self.set_active_state()
       
    def move_forward_right(self):
        self.inputs_to_activate = ['lf']
        self.set_active_state()
    
    def move_backword_left(self):
        self.inputs_to_activate = ['lb']
        self.set_active_state()
    
    def move_backword_right(self):
        self.inputs_to_activate = ['rb']
        self.set_active_state()
    
    def stop(self):
        self.inputs_to_activate = []
        self.set_active_state()

    def change_speed(self,speed):
        if speed in self.speeds:
            self.rep.ChangeDutyCycle(self.speeds[speed])
            self.lep.ChangeDutyCycle(self.speeds[speed])
