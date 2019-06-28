# pages/views.py
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from tank import *

TM = Tank.getInstance()	

def start_streaming(request):
	try:
		main()
	except Exception as e:
		result =  {"status": "failed", "output":str(e)}
		html = "<html><body>Script status: %s \n Output: %s</body></html>" %(result['status'],result['output'])
		return HttpResponse(html)

def stream(request):
	return render(request, 'camera.html')

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



