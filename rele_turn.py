#!/usr/bin/env python

# Command:
#  ./rele_turn.py pin on/off
#
# where on and off means normally closed and opened (because cables
# were mounted to be normally closed as default).
#
# Example:
#  rele_turn.py  4 1 # turn on  p-supply rpi-cam + tinesyne-amp
#  rele_turn.py 17 1 # turn on  p-supply rpi-studio
#  rele_turn.py 27 1 # turn on  empty
#  rele_turn.py 22 1 # turn on  empty
#  rele_turn.py  4 0 # turn off p-supply rpi-cam + tinesyne-amp
#  rele_turn.py 17 0 # turn off p-supply rpi-studio
#  rele_turn.py 27 0 # turn off empty
#  rele_turn.py 22 0 # turn off empty

import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)

PIN_RELE = int(sys.argv[1])

GPIO.setmode(GPIO.BCM)   # referring to the pins by the "Broadcom SOC channel" number, these are the numbers after "GPIO"
#GPIO.setmode(GPIO.BOARD)# referring to the pins by the number of the pin the the plug

# Set GPIO to output
GPIO.setup(PIN_RELE, GPIO.OUT, initial=True)
#GPIO.setup(PIN_RELE,GPIO.OUT)

if int(sys.argv[2])==0:
  print "Rele :: opened contact"
  GPIO.output(PIN_RELE,GPIO.LOW)
else:
  print "Rele :: closed contact"
  GPIO.output(PIN_RELE,GPIO.HIGH)
