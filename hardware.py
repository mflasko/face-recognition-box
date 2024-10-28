from gpiozero import Button, LED, Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import time
import cv2
import config




class Box():
    def __init__(self, model):
        self.box_green_led = LED(config.GREEN_LED_PIN)
        self.box_red_led = LED(config.RED_LED_PIN)
        self.box_button = Button(config.BUTTON_PIN)
        self.box_servo = Servo(config.SERVO_PIN)
        
		# Initialize camera
        self.camera = config.get_camera()
        # the model to use for face recognization 
        self.model = model
		
        self.box_button.when_held = self.button_held
        self.box_button.when_released = self.button_released

    def button_held(self, btn):
        #global pressTime
        btn.was_held = True
        self.try_lock_box()
        #print("button was held not just pressed")
        #print(f"presstime: {pressTime} \n")

    def button_released(self, btn):
        global pressTime
        if not btn.was_held:
            self.button_pressed(btn)
        #else:
        #    print("button released no press called")
        btn.was_held = False
        pressTime = time.time()
        #print(f"presstime: {pressTime} \n")

    def button_pressed(self, btn):
        global pressTime
        newTime = time.time()
        timeDiff = newTime - pressTime
        if timeDiff > 1:
            #no button bounce
            pressTime = newTime
            self.try_unlock_box()
            #print("button was pressed not held \n")

    def try_lock_box(self):
        #TODO: move servo 
        self.box_servo.max()

    def try_unlock_box(self):
        if True:
        #if self.is_face_detected():
            self.blink_LED(self.box_green_led, 3)
            #TODO: unlock box servo change
            #print("face detected; unlocked box")		
        else:
            self.blink_LED(self.box_red_led, 3)
            #print('face not detected blinked red LED')

    def blink_LED(self, led, count):
        for i in range(count):
            led.blink()

    def is_face_detected(self):
        print('taking picture using the camera')
        # Check for the positive face and unlock if found.
        img = self.camera.read()
        
        print("Captured image from camera")
        cv2.imshow('color image from camera', img)
        key = cv2.waitKey(0)
        if key == 27: # if ESC is pressed, exit loop
            cv2.destroyAllWindows()
        #print('Converting image to greyscale')
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
        else:
            print(f"# faces detected: {len(faces_rect)}")
            x, y, w, h = faces_rect[0]			
            # Crop and resize image to face.
            crop = face.resize(face.crop(gray_img, x, y, w, h))
            # Test face against model.
            label, confidence = model.predict(crop)
            print(f"Predicted {'POSITIVE' if label == config.POSITIVE_LABEL else 'NEGATIVE'} face with confidence {confidence} (lower is more confident).")
        #if label == config.POSITIVE_LABEL and confidence < config.POSITIVE_THRESHOLD:
        if label == config.POSITIVE_LABEL:
            print ("Recognized face!")
            return True
        else:
            print ("Did not recognize face!")
            return False

