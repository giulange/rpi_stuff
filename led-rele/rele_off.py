#!/usr/bin/python

import RPi.GPIO as GPIO

# use pin number from 1 to 40:
GPIO.setmode(GPIO.BOARD)

GPIO.cleanup()

GPIO.setup(5,GPIO.OUT)

GPIO.output(5,False)

print "Light state turned!" # print everything fine!

#GPIO.cleanup()
