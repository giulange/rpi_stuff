#!/usr/bin/python

# for pin GPIO17 you give in input 17

import sys
pinLED=int( sys.argv[1] )

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(pinLED,GPIO.OUT)

GPIO.output(pinLED,True)

GPIO.cleanup() # this ensures a clean exit

