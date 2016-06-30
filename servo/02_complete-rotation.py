# see this link :: http://www.toptechboy.com/raspberry-pi/raspberry-pi-lesson-28-controlling-a-servo-on-raspberry-pi-with-python/
# see README for connections

# I tested my servo and DutyCycle spans from 3 to 13

OPIN 		= 11
f 		= 50 		# signal frequency [Hz]
FullLeft	= 3
FullRight	= 13
Middle 		= 8

import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode( GPIO.BOARD )

GPIO.setup( OPIN, GPIO.OUT )

pwm = GPIO.PWM( OPIN, f )



# DutyCycle = PulseWidth/Period = PulseWidth * f
#FL        	= FullLeft  /(50*100)	# Full Left  Position : PulseWidth=0.6ms
#Mi          	= Middle    /(50*100)	# Middle     Position : PulseWidth=1.6ms
#FR       	= FullRight /(50*100)	# Full Right Position : PulseWidth=2.6ms

#pwm.start( f * Mi *100  )
pwm.start( Middle  )

#mi 		= int(Mi*10000)
#fl		= int(FL*10000)
#fr		= int(FR*10000)

#print 'mi=' + str(mi)
#print 'fl=' + str(fl)
#print 'fr=' + str(fr)

#for dc in range( mi, fl-1, -1 ):
for dc in range( Middle, FullLeft-1, -1 ):
  print 'DutyCycle = ' + str( dc )
#  print( "{0:.4f}".format( f * (float(dc)/10000) *100 ) )
#  print( "{0:.4f}".format( 0.0006 ) )
#  pwm.ChangeDutyCycle( f * (dc/10000) *100 )
  pwm.ChangeDutyCycle( dc )
  time.sleep( 0.5 )

#pwm.ChangeDutyCycle( f * Middle *100 )
#pwm.ChangeDutyCycle( f * FullRight *100 )

print 'DutyCycle = ' + str( Middle )
pwm.ChangeDutyCycle( Middle )

print 'End!'
