"""Raspberry Pi Face Recognition Treasure Box
Treasure Box Script
Copyright 2013 Tony DiCola 
"""
import cv2

import config
import face
import hardware


if __name__ == '__main__':
	# Load training data into model
	print ("Loading training data...")
	#model = cv2.createEigenFaceRecognizer()
	model = cv2.face.EigenFaceRecognizer_create()
	#model.load(config.TRAINING_FILE)
	model.read(config.TRAINING_FILE)
	print ("Training data loaded!")
	# Initialize camer and box.
	camera = config.get_camera()
	box = hardware.Box()
	# Move box to locked position.
	box.lock()
	print ("Running box...")
	print ("Press button to lock (if unlocked), or unlock if the correct face is detected.")
	print ("Press Ctrl-C to quit.")
	while True:
		# Check if capture should be made.
		# TODO: Check if button is pressed.
		if box.is_button_up():
			#if not box.is_locked:
			if not box.is_box_locked():
				# Lock the box if it is unlocked
				box.lock()
				print ("Box is now locked.")
			else:
				print ("Button pressed, looking for face...")
				# Check for the positive face and unlock if found.
				img = camera.read()
				# Convert image to grayscale.
				#image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
				# Get coordinates of single face in captured image.
				#result = face.detect_single(image)  // old

				print("DEBUG: captured image from camera")
				cv2.imshow('color image from camera', img)
				key = cv2.waitKey(0)
				if key == 27: # if ESC is pressed, exit loop
					cv2.destroyAllWindows()

				print('DEBUG: onto greyscaling')
				gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
				cv2.imshow('greyscale file from camera', gray_img)
				key = cv2.waitKey(0)
				if key == 27: # if ESC is pressed, exit loop
					cv2.destroyAllWindows()	

				#config.HAAR_FACES
				haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
				faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9) 
				if len(faces_rect) < 1:
					print ("Could not detect single face!  Check the image in capture.pgm' \
					  ' to see what was captured and try again with only one face visible.")
					continue
				else:
					print(f"# faces detected: {len(faces_rect)}")

				x, y, w, h = faces_rect[0]			

				#if result is None:
				#	print ("Could not detect single face!  Check the image in capture.pgm' \
				#		  ' to see what was captured and try again with only one face visible.")
				#	continue
				#x, y, w, h = result
				
				# Crop and resize image to face.
				crop = face.resize(face.crop(gray_img, x, y, w, h))
				# Test face against model.
				label, confidence = model.predict(crop)
				print(f"Predicted {'POSITIVE' if label == config.POSITIVE_LABEL else 'NEGATIVE'} face with confidence {confidence} (lower is more confident).")
				#if label == config.POSITIVE_LABEL and confidence < config.POSITIVE_THRESHOLD:
				if label == config.POSITIVE_LABEL:
					print ("Recognized face!")
					box.unlock()
				else:
					print ("Did not recognize face!")
				
				input("press enter to continue ....")