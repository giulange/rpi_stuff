# see this link :: http://www.toptechboy.com/raspberry-pi/raspberry-pi-lesson-28-controlling-a-servo-on-raspberry-pi-with-python/
# see README for connections

# I tested my servo and DutyCycle spans from 2 to 12

OPIN 		= 11
f 		= 50 		# signal frequency [Hz]
FullLeft 	= 0.0010	# Full Left  Position : PulseWidth=1.0ms
Middle		= 0.0015	# Middle     Position : PulseWidth=1.5ms
FullRight	= 0.0020	# Full Right Position : PulseWidth=2.0ms


import RPi.GPIO as GPIO

GPIO.setmode( GPIO.BOARD )

GPIO.setup( OPIN, GPIO.OUT )

pwm = GPIO.PWM( OPIN, f )

# DutyCycle = PulseWidth/Period = PulseWidth * f

pwm.start( f * FullLeft *10  )

#pwm.ChangeDutyCycle( f * Middle *10  )
#pwm.start( f * Middle *10  )

#pwm.ChangeDutyCycle( f * FullRight *10 )
#pwm.start( f * FullRight *10 )



#pwm.start( 2  )
#pwm.start( 3  )
#pwm.start( 4  )
#pwm.start( 5  )
#pwm.start( 6  )
#pwm.start( 7  )
#pwm.start( 8  )
#pwm.start( 9  )
#pwm.start( 10  )
#pwm.start( 11  )
#pwm.start( 12  )



