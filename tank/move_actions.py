from tank import GPIO
from tank.move_functions import move_forward, move_backword, stop, move_forward_left ,move_forward_right, move_backword_left, move_backword_right, change_speed

print("s-stop \nf-forward \nfr-forward right \nfl-forward left \nb-backward \nl-low \nm-medium \nh-high \ne-exit")

while(1):

    x=input()

    if x=='s':
        stop()
    elif x=='f':
        move_forward()
    elif x=='b':
        move_backword()
    elif x=='fl':
        move_forward_left()
    elif x=='fr':
        move_forward_right()
    elif x=='bl':
        move_backword_left()
    elif x=='br':
        move_backword_right()
    elif x=='l':
        change_speed('low')
    elif x=='m':
        change_speed('medium')
    elif x=='h':
        change_speed('high')
    elif x=='e':
        GPIO.cleanup()
        break
    else:
        print("we don't have this option!!")
        print("please enter the defined data to continue.....")
