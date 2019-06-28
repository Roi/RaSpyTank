from tank import GPIO
from tank.gpio_settings import speeds,IM,rep,lep

def move_forward():
    print("forward")
    GPIO.output(IM['rf'],GPIO.HIGH)
    GPIO.output(IM['lf'],GPIO.HIGH)
    GPIO.output(IM['rb'],GPIO.LOW)
    GPIO.output(IM['lb'],GPIO.LOW)

def move_backword():
    print("backward")
    GPIO.output(IM['rf'],GPIO.LOW)
    GPIO.output(IM['lf'],GPIO.LOW)
    GPIO.output(IM['rb'],GPIO.HIGH)
    GPIO.output(IM['lb'],GPIO.HIGH)

def move_forward_left():
    print("forward-left")
    GPIO.output(IM['rf'],GPIO.HIGH)
    GPIO.output(IM['lf'],GPIO.LOW)
    GPIO.output(IM['rb'],GPIO.LOW)
    GPIO.output(IM['lb'],GPIO.LOW)

def move_forward_right():
    print("forward-right")
    GPIO.output(IM['rf'],GPIO.LOW)
    GPIO.output(IM['lf'],GPIO.HIGH)
    GPIO.output(IM['rb'],GPIO.LOW)
    GPIO.output(IM['lb'],GPIO.LOW)

def move_backword_left():
    print("backward-left")
    GPIO.output(IM['rf'],GPIO.LOW)
    GPIO.output(IM['lf'],GPIO.LOW)
    GPIO.output(IM['rb'],GPIO.LOW)
    GPIO.output(IM['lb'],GPIO.HIGH)

def move_backword_right():
    print("backward-right")
    GPIO.output(IM['rf'],GPIO.LOW)
    GPIO.output(IM['lf'],GPIO.LOW)
    GPIO.output(IM['rb'],GPIO.HIGH)
    GPIO.output(IM['lb'],GPIO.LOW)

def stop():
    print("stop")
    GPIO.output(IM['rf'],GPIO.LOW)
    GPIO.output(IM['lf'],GPIO.LOW)
    GPIO.output(IM['rb'],GPIO.LOW)
    GPIO.output(IM['lb'],GPIO.LOW)

def change_speed(speed):
    if speed in speeds:
        print(speed)
        rep.ChangeDutyCycle(speeds[speed])
        lep.ChangeDutyCycle(speeds[speed])
