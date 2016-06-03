#!/usr/bin/python
# Author: 	Giuliano Langella 
# Email:	gyuliano@libero.it

import sys
import RPi.GPIO as GPIO
import time
import datetime 
import Adafruit_DHT

DHT_TYPE		= 11
DHT_GPIOPIN 		= 14 
LED_GPIOPIN		= 3
FREQUENCY_SECONDS	= 10	# How long to wait (in seconds) between measurements.
FREQUENCY_SKIP		= 6

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_GPIOPIN,GPIO.OUT)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).  
# If this happens try again!

print "\n\n"

while True:

	# Try to grab a sensor reading.  Use the read_retry method which will retry up
	# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
	GPIO.output(LED_GPIOPIN,True)
	humidity, temperature = Adafruit_DHT.read(DHT_TYPE, DHT_GPIOPIN)
	NOW = datetime.datetime.now()
	
	if humidity is None and temperature is None:
		print 'skip'
		GPIO.output(LED_GPIOPIN,False)
		time.sleep(FREQUENCY_SKIP)
		continue
		
	#print datetime.datetime.now().strftime("%Y-%b-%d %H:%M:%S")
	print datetime.datetime.now().strftime("%Y-%b-%d %H:%M:%S") + '\tTemp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
	GPIO.output(LED_GPIOPIN,False)
	time.sleep(FREQUENCY_SECONDS)

