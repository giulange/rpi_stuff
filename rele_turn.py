#!/usr/bin/env python

# Command:
#  ./rele_turn.py pin on/off rpiv
#
# where:
#    - pin is the GPIO pin number
#    - on and off means normally closed and opened (because cables
# were mounted to be normally closed as default)
#    - rpiv is the last 8-bit IP number (e.g. 36 for parents)
#
# Example:
#  rele_turn.py  4 1 # turn on  p-supply rpi-cam + tinesyne-amp
#  rele_turn.py 17 1 # turn on  p-supply rpi-studio
#  rele_turn.py  4 0 36 # turn off p-supply rpi-cam + tinesyne-amp
#  rele_turn.py 17 0 36 # turn off p-supply rpi-studio

# this is useful to poweroff the rpiv before to turn off the power supply:
#from subprocess import call

import RPi.GPIO as GPIO
import time
import sys
import os

GPIO.setwarnings(False)

PIN_RELE = int(sys.argv[1])

GPIO.setmode(GPIO.BCM)   # referring to the pins by the "Broadcom SOC channel" number, these are the numbers after "GPIO"
#GPIO.setmode(GPIO.BOARD)# referring to the pins by the number of the pin the the plug

# PARs
PAUSE_1 = 1
PAUSE_2 = 10

IP  = 'pi@192.168.1.' + sys.argv[3]
CMD = 'ssh ' + IP + ' sudo poweroff &'

# Set GPIO to output
GPIO.setup(PIN_RELE, GPIO.OUT, initial=True)
#GPIO.setup(PIN_RELE,GPIO.OUT)

if int(sys.argv[2])==0:
  print "powering on the rpiv: " + IP
  GPIO.output(PIN_RELE,GPIO.LOW)
  time.sleep( PAUSE_1 )
  print "Rele :: opened contact"
else:
  print "powering off the rpiv: " + IP
 #call(['ssh',IP,'sudo poweroff'])
  x = os.system( CMD )
  time.sleep( PAUSE_2 )
  GPIO.output(PIN_RELE,GPIO.HIGH)
  print "Rele :: closed contact"


