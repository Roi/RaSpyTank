from tank import GPIO 
from tank import TankGPIO
from tank import time

class TankMove(TankGPIO):
    def __init__(self):
        TankGPIO.__init__(self)
        self.inputs_to_activate = []
        self.init_gpio()
        self.rep = GPIO.PWM(self.inputsMapping['outputs']['motor']['engine']['re'], 1000) #right_engine pwm
        self.lep = GPIO.PWM(self.inputsMapping['outputs']['motor']['engine']['le'], 1000) #left_engine pwm
        self.rep.start(50)
        self.lep.start(50)

    def init_gpio(self):    
        GPIO.setmode(GPIO.BOARD)
        #GPIO.setwarnings(False)
        
        outputs = list(self.inputsMapping['outputs']['motor']['directions'].values()) + list(self.inputsMapping['outputs']['motor']['engine'].values()) + list(self.inputsMapping['outputs']['sensors']['distance'].values())
        
        for OP in outputs:
            GPIO.setup(OP, GPIO.OUT)
        
        for SI in self.inputsMapping['inputs']['sensors']['distance'].values():
            GPIO.setup(SI, GPIO.IN)

        for DI in self.inputsMapping['outputs']['motor']['directions'].values():
            GPIO.output(DI, GPIO.LOW)

        GPIO.output(self.inputsMapping['outputs']['sensors']['distance']['tr'], GPIO.LOW)
        

    def calc_distance(self):
        
        GPIO.output(self.inputsMapping['outputs']['sensors']['distance']['tr'], GPIO.LOW)

        #time.sleep(2)
        
        GPIO.output(self.inputsMapping['outputs']['sensors']['distance']['tr'], GPIO.HIGH)

        time.sleep(0.00001)

        GPIO.output(self.inputsMapping['outputs']['sensors']['distance']['tr'], GPIO.LOW)

        while GPIO.input(self.inputsMapping['inputs']['sensors']['distance']['ec'])==0:
            pulse_start_time = time.time()
        while GPIO.input(self.inputsMapping['inputs']['sensors']['distance']['ec'])==1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round( ( pulse_duration * 17150 ) / 100, 2)
        
        return distance

    def is_channel_in_use(self,channel):
        return GPIO.input(channel)

    def set_active_state(self):
        for inp in self.inputsMapping['outputs']['motor']['directions'].keys():
            if inp in self.inputs_to_activate:
                GPIO.output(self.inputsMapping['outputs']['motor']['directions'][inp], GPIO.HIGH)
            else:
                GPIO.output(self.inputsMapping['outputs']['motor']['directions'][inp], GPIO.LOW)
         
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
