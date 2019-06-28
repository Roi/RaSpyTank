from tank import GPIO

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

speeds=  dict()
speeds['low'] = 25
speeds['medium'] = 50
speeds['high'] = 75

IM =  dict() #InputsMapping
IM['rb'] = 12 #right_back
IM['rf']  = 11 #right_forward
IM['re'] = 18 #right_engine
IM['lb']  = 13 #left_back
IM['lf']   = 15 #left_forward
IM['le']  = 16 #left_engine

Inputs = [ 'rb', 'rf', 're', 'lb', 'lf', 'le' ]
EngineInputs = ['re','le']

for inp in Inputs:
        if inp in IM:
                GPIO.setup(IM[inp], GPIO.OUT)
                if inp not in EngineInputs:
                        GPIO.output(IM[inp], GPIO.LOW)

rep = GPIO.PWM(IM['re'], 1000)  # right engine pwm
lep = GPIO.PWM(IM['le'], 1000)  # left engine pwm
rep.start(50)
lep.start(50)