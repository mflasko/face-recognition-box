"""Raspberry Pi Face Recognition Treasure Box
Positive Image Capture Script
Copyright 2013 Tony DiCola 

Run this script to capture positive images for training the face recognizer.
"""
import glob
import os
import sys
import select

import cv2

import hardware
import config
import face


# Prefix for positive training image filenames.
POSITIVE_FILE_PREFIX = 'positive_'


def is_letter_input(letter):
	# Utility function to check if a specific character is available on stdin.
	# Comparison is case insensitive.
	if select.select([sys.stdin,],[],[],0.0)[0]:
		input_char = sys.stdin.read(1)
		return input_char.lower() == letter.lower()
	return False


if __name__ == '__main__':
	camera = config.get_camera()
	box = hardware.Box()
	# Create the directory for positive training images if it doesn't exist.
	if not os.path.exists(config.POSITIVE_DIR):
		os.makedirs(config.POSITIVE_DIR)
	# Find the largest ID of existing positive images.
	# Start new images after this ID value.
	files = sorted(glob.glob(os.path.join(config.POSITIVE_DIR, 
		POSITIVE_FILE_PREFIX + '[0-9][0-9][0-9].pgm')))
	count = 0
	if len(files) > 0:
		# Grab the count from the last filename.
		count = int(files[-1][-7:-4])+1
	print ('Capturing positive training images.')
	print ('Press button or type c (and press enter) to capture an image.')
	print ('Press Ctrl-C to quit.')
	while True:
		# Check if button was pressed or 'c' was received, then capture image.
		if box.is_button_up() or is_letter_input('c'):
			print ('Capturing image...')
			img = camera.read()
			
			# Convert image to grayscale.
			#image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
			# Get coordinates of single face in captured image.

			print('DEBUG: onto greyscaling')
			gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			print("DEBUG: image show called")
			cv2.imshow('greyscale file from camera', gray_img)
			key = cv2.waitKey(0)
			if key == 27: # if ESC is pressed, exit loop
				cv2.destroyAllWindows()	
			
			#config.HAAR_FACES
			haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
			faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9) 
			if len(faces_rect) < 1:
				print("No face detected")
			else:
				print(f"# faces detected: {len(faces_rect)}")
			for (x, y, w, h) in faces_rect: 
				cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

			cv2.imshow('Detected faces', img)
			key = cv2.waitKey(0)
			if key == 27: # if ESC is pressed, exit loop
				cv2.destroyAllWindows()

			print ("calling face crop:", x, y, w, h)
			#crop image 
			crop = face.crop(img, x, y, w, h)

			"""
			result = face.detect_single(image)
			if result is None:
				print ('Could not detect single face!  Check the image in capture.pgm' \
					  ' to see what was captured and try again with only one face visible.')
				continue
			x, y, w, h = result
			# Crop image as close as possible to desired face aspect ratio.
			# Might be smaller if face is near edge of image.
			crop = face.crop(image, x, y, w, h)
			"""

			# Save image to file.
			filename = os.path.join(config.POSITIVE_DIR, POSITIVE_FILE_PREFIX + '%03d.pgm' % count)
			cv2.imwrite(filename, crop)
			print ('Found face and wrote training image', filename)
			count += 1
