OPIN 		= 11
f 		= 50 		# signal frequency [Hz]
Middle 		= 8

import RPi.GPIO as GPIO

GPIO.setmode( GPIO.BOARD )

GPIO.setup( OPIN, GPIO.OUT )

pwm = GPIO.PWM( OPIN, f )

pwm.start( Middle  )

