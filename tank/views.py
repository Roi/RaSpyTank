# pages/views.py
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from tank import GPIO
from tank import time
from tank import TankMove
from tank import TankGPIO
from tank import Tank

TM = Tank.getInstance()	

def index(request):
	return render(request, 'index.html')


def move(request):
	
	action = request.GET.get("action")
	
	x =  action
	if x=='s':
		TM.stop()
	elif x=='f':
		TM.move_forward()
	elif x=='b':
		TM.move_backword()
	elif x=='fl':
		TM.move_forward_left()
	elif x=='fr':
		TM.move_forward_right()
	elif x=='bl':
		TM.move_backword_left()
	elif x=='br':
		TM.move_backword_right()
	elif x=='l':
		TM.change_speed('low')
	elif x=='m':
		TM.change_speed('medium')
	elif x=='h':
		TM.change_speed('high')
	elif x=='e':
		GPIO.cleanup()
	elif x=='re':
		TM.init_gpio()

	
	return HttpResponse('Your Action is : ' + TM.actions[action] )



