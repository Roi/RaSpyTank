import RPi.GPIO as GPIO
import time
from .gpio_settings import speeds,IM,rep,lep
from .move_functions import move_forward, move_backword, stop, move_forward_left ,move_forward_right, move_backword_left, move_backword_right, change_speed
