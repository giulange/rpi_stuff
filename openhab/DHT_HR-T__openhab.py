#!/usr/bin/python
# Author: 	Giuliano Langella 
# Email:	gyuliano@libero.it

import sys
import RPi.GPIO as GPIO
import time
import Adafruit_DHT

DHT_TYPE		= 11
DHT_GPIOPIN 		= sys.argv[1] 
FREQUENCY_SKIP		= 2

GPIO.setmode(GPIO.BOARD)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).  
# If this happens try again!


# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read(DHT_TYPE, DHT_GPIOPIN)

while humidity is None and temperature is None:
	humidity, temperature = Adafruit_DHT.read(DHT_TYPE, DHT_GPIOPIN)
	time.sleep(FREQUENCY_SKIP)
	
#print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
if sys.argv[2]=='TEMP':
	print '{0:0.1f}'.format(temperature)
if sys.argv[2]=='HUM':
	print '{0:0.1f}'.format(humidity)

