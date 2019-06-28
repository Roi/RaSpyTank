"""
WSGI config for tank project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
import os
import sys
import platform

from django.core.wsgi import get_wsgi_application

plt = platform.system()

if plt =="Windows":
    sys_path = 'c:/wamp64/www/tank/camera/'
elif plt =="Linux":
    sys_path = '/var/www/html/tank/camera/'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'camera.settings')

application = get_wsgi_application()
