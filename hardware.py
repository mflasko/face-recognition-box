"""Raspberry Pi Face Recognition Treasure Box
Treasure Box Class
Copyright 2013 Tony DiCola 
"""
import time

import cv2
#import RPIO
#from RPIO import PWM
from gpiozero import Button, LED, Servo

import picam
import config
import face


class Box(object):
	"""Class to represent the state and encapsulate access to the hardware of 
	the treasure box."""
	def __init__(self):
		# Initialize lock servo and button.
		#self.servo = PWM.Servo()
		# code from: https://www.raspberrypi-spy.co.uk/2018/02/basic-servo-use-with-the-raspberry-pi/
		self.servo = Servo(config.LOCK_SERVO_PIN) #likely more to do here 
		
		
		self.button = Button(config.BUTTON_PIN)
		
		# original code
		#RPIO.setup(config.BUTTON_PIN, RPIO.IN)
		# Set initial box state.
		#self.button_state = RPIO.input(config.BUTTON_PIN)
		#self.is_locked = None

	def lock(self):
		"""Lock the box."""
		"""
		self.servo.set_servo(config.LOCK_SERVO_PIN, config.LOCK_SERVO_LOCKED)
		self.is_locked = True
		"""
		
	def unlock(self):
		"""Unlock the box."""
		"""
		self.servo.set_servo(config.LOCK_SERVO_PIN, config.LOCK_SERVO_UNLOCKED)
		self.is_locked = False
		"""

	def is_button_up(self):
		"""Return True when the box button has transitioned from down to up (i.e.
		the button was pressed)."""
		#commented out so will run 
		#old_state = self.button_state
		#self.button_state = RPIO.input(config.BUTTON_PIN)
		
		# Check if transition from down to up
		
		
		"""
		if old_state == config.BUTTON_DOWN and self.button_state == config.BUTTON_UP:
			# Wait 20 milliseconds and measure again to debounce switch.
			time.sleep(20.0/1000.0)
			#self.button_state = RPIO.input(config.BUTTON_PIN)
			if self.button_state == config.BUTTON_UP:
				return True
		return False
		"""

		return True