#!/usr/bin/python

import RPi.GPIO as GPIO

channel=5
print "channel: ",channel

# use pin number from 1 to 40:
GPIO.setmode(GPIO.BOARD)

GPIO.input(5)

#GPIO.setup(5,GPIO.OUT)

#GPIO.output(5,False)

#print "Light state turned!" # print everything fine!

#GPIO.cleanup()
