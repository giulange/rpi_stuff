#!/usr/bin/python

import RPi.GPIO as GPIO

try:
    # use pin number from 1 to 40:
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(5,GPIO.OUT)

    GPIO.output(5,False)
    print "Light state turned!" # print everything fine!

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print "keyboard interruption" # print antthing you want
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print "Other error or exception occurred!"  
  
finally:  
    GPIO.cleanup() # this ensures a clean exit  
