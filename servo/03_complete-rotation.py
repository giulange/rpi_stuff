# see this link :: http://www.toptechboy.com/raspberry-pi/raspberry-pi-lesson-28-controlling-a-servo-on-raspberry-pi-with-python/
# see README for connections

# I tested my servo and DutyCycle spans from 3 to 13

OPIN 		= 11
f 		= 50 		# signal frequency [Hz]
PAUSE		= 0.20 		# 0.05
FACTOR		= 10.0
FullLeft	= 3
FullRight	= 13
Middle 		= 8

import RPi.GPIO as GPIO
import time
import sys
#from __future__ import division # to allow division with floats

GPIO.setmode( GPIO.BOARD )

GPIO.setup( OPIN, GPIO.OUT )

pwm = GPIO.PWM( OPIN, f )


pwm.start( Middle  )

for dc in range( Middle*int(FACTOR), (FullLeft-0)*int(FACTOR), -1 ):
  print 'DutyCycle = ' + str( dc/FACTOR )
#  print("{0:.2f}".format( float(dc/FACTOR) ))
  pwm.ChangeDutyCycle( float(dc/FACTOR) )
  time.sleep( PAUSE )

for dc in range( FullLeft*int(FACTOR), FullRight*int(FACTOR), +1 ):
  print 'DutyCycle = ' + str( dc/FACTOR )
  pwm.ChangeDutyCycle( float(dc/FACTOR) )
  time.sleep( PAUSE )

for dc in range( FullRight*int(FACTOR), Middle*int(FACTOR), -1 ):
  print 'DutyCycle = ' + str( dc/FACTOR )
  pwm.ChangeDutyCycle( float(dc/FACTOR) )
  time.sleep( PAUSE )

print( 'End!' )
