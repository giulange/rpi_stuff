#!/usr/bin/python3

from gpiozero import MotionSensor
import time

# Out pin (3.3V) is on GPIO17:
pinOut = 17

pir = MotionSensor(pinOut)
while True:
  ii = 0
  if pir.motion_detected:
    ii = ii +1
    print("Motion detected! [%d]" % ii)
    #time.sleep(100)
	

