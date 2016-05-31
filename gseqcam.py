#!/usr/bin/python
# Author: 	Giuliano Langella 
# Email:	gyuliano@libero.it

import picamera
from time import sleep
import datetime

camera = picamera.PiCamera()

# DEF cam properties;
camera.sharpness 		= 0
camera.contrast			= 0
camera.brightness		= 50
camera.saturation		= 0
camera.ISO 			= 0
camera.video_stabilization 	= False
camera.exposure_compensation 	= 0
camera.exposure_mode 		= 'auto'
camera.meter_mode 		= 'average'
camera.awb_mode 		= 'auto'
camera.image_effect 		= 'none'
camera.color_effects	 	= None
camera.rotation 		= 0
camera.hflip 			= False
camera.vflip 			= False
camera.crop 			= (0.0, 0.0, 1.0, 1.0)

#DEF
numTimes 			= 4;
sleepTime			= 0;

#camera.capture_sequence(['/home/pi/scripts/cam-shots/img' + datetime.datetime.now().strftime("%Y%b%d_%H%M%S") + '.jpg' i for i in range(2)])

for i in range(0,numTimes):
	camera.capture('/home/pi/scripts/cam-shots/img' + datetime.datetime.now().strftime("%Y%b%d_%H%M%S") + '.jpg')
	sleep(sleepTime)

