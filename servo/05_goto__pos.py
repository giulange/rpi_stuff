#!/usr/bin/python

import sys
import RPi.GPIO as GPIO

OPIN 		= 11
f 		= 50 		# signal frequency [Hz]
Position	= float( sys.argv[1] )

#print( Position )

GPIO.setwarnings(False)

GPIO.setmode( GPIO.BOARD )

GPIO.setup( OPIN, GPIO.OUT )

pwm = GPIO.PWM( OPIN, f )

pwm.start( Position )

