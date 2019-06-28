# pages/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from subprocess import Popen, PIPE, STDOUT

def index(request):
    command = ["bash","/var/www/html/tank/camera/stream.sh"]
    try:
            process = Popen(command, stdout=PIPE, stderr=STDOUT)
            output = process.stdout.read()
            exitstatus = process.poll()
            if (exitstatus==0):
                    result = {"status": "Success", "output":str(output)}
            else:
                    result = {"status": "Failed", "output":str(output)}

    except Exception as e:
            result =  {"status": "failed", "output":str(e)}

    html = "<html><body>Script status: %s \n Output: %s</body></html>" %(result['status'],result['output'])
    #return HttpResponse(html)
    return render(request,'camera.html',{})