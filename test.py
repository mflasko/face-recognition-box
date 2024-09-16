"""Raspberry Pi Face Recognition Treasure Box
Treasure Box Script
Copyright 2013 Tony DiCola 
"""
#import cv2
import time
import config
#import face
import hardware
from gpiozero import Button, LED, Servo

global tp

def button_pressed():
	tp = time.time()
	box.blink_green_led(1)

def button_released():
	tr = time.time()
	time_diff = int(tr - tp)


if __name__ == '__main__':
	camera = config.get_camera()
	#box = hardware.Box()
	
	print ("Running box...")
	print ("Press button to lock (if unlocked), or unlock if the correct face is detected.")
	print ("Press Ctrl-C to quit.")

	#box.button.when_pressed = button_pressed
	#box.button.when_released = button_released

	red = LED(17)
	green = LED(27)	
	buttontest = Button(2)
	print('green led on')
	green.on()
	time.sleep(10)
	print('green off')
	green.off()
	print('red LED OFF')
	red.off()
	while True:
		time.sleep(2)
		print ('looping')

'''
	while True:
		print('loop started')
		if buttontest.is_pressed:
			print("Button is pressed")
		else:
			print("Button is not pressed")
		
		red.on()
		time.sleep(1)
		red.off()

		green.on()
		time.sleep(1)
		green.off()

'''