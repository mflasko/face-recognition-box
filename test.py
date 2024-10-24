import time
from gpiozero import Button, LED, Servo, Device
from gpiozero.pins.pigpio import PiGPIOFactory

pressTime = 0

Device.pin_factory = PiGPIOFactory()

Button.was_held = False


def held(btn):
    global pressTime
    btn.was_held = True
    print("button was held not just pressed")
    #print(f"presstime: {pressTime} \n")

def released(btn):
    global pressTime
    if not btn.was_held:
        pressed(btn)
    #else:
    #    print("button released no press called")
        
    btn.was_held = False
    pressTime = time.time()
    #print(f"presstime: {pressTime} \n")

def pressed(btn):
    global pressTime
    newTime = time.time()
    timeDiff = newTime - pressTime
    #print(f"button pressed entered -- presstime:{pressTime} ; timeDiff:{timeDiff}")
    if timeDiff > 1:
        #no button bounce - valid second press
        pressTime = newTime
        print("button was pressed not held \n")

if __name__ == '__main__':
    print ('running box')
    print ("Press button to lock (if unlocked), or unlock if the correct face is detected.")
    print ("Press Ctrl-C to quit.")
    green = LED(17)
    btn = Button(27)
    servo = Servo(25)
        
    btn.when_held = held
    btn.when_released = released

    while True:
        green.on()
        print('green on')
        time.sleep(2)
        green.off()
        print('green off')
        servo.min()
        time.sleep(2)
        servo.mid()
        time.sleep(2)
        servo.max()
        time.sleep(2)
