#!/usr/bin/python

import RPi.GPIO as GPIO
import sys

pinLED=int( sys.argv[1] )

GPIO.setmode(GPIO.BCM)

GPIO.setup(pinLED,GPIO.OUT)

GPIO.output(pinLED,False)

GPIO.cleanup() # this ensures a clean exit
