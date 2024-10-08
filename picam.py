"""Raspberry Pi Face Recognition Treasure Box 
Pi Camera OpenCV Capture Device
Copyright 2013 Tony DiCola 

Pi camera device capture class for OpenCV.  This class allows you to capture a
single image from the pi camera as an OpenCV image.
"""
import io
import time

import cv2
import numpy as np
#import picamera 
from picamera2 import Picamera2
import time

import config

class OpenCVCapture(object):
	#picam2 = Picamera2()
	def read(self):
		"""Read a single frame from the camera and return the data as an OpenCV
		image (which is a numpy array).
		"""
		# This code is based on the picamera example at:
		# http://picamera.readthedocs.org/en/release-1.0/recipes1.html#capturing-to-an-opencv-object
		# Capture a frame from the camera.
		data = io.BytesIO()
		#with picamera.PiCamera() as camera:
		#	camera.capture(data, format='jpeg')

		#upgrade to picamera2 code: 
		#picam2 = Picamera2()
		with Picamera2() as picam2:
			picam2.preview_configuration.main.format = "RGB888"
			picam2.start()
			time.sleep(2)
			img = picam2.capture_array()  #returns numpy array 
		#picam2.capture_file("capture.jpg")
		#img = cv2.imread('capture.jpg')
		
			picam2.stop()
			time.sleep(2)
						
		#data = np.fromstring(data.getvalue(), dtype=np.uint8)
		# Decode the image data and return an OpenCV image.
		#image = cv2.imdecode(data, 1)

		#updated below after picamera2 changes
		# Save captured image for debugging#.
		#cv2.imwrite(config.DEBUG_IMAGE, img_array)
		# Return the captured image data.
		return img
