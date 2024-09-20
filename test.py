import time
from gpiozero import Button, LED

global tp

#Button.was_held = False

def held(btn):
    btn.was_held = True
    print("button was held not just pressed")

def released(btn):
    if not btn.was_held:
        pressed()
    btn.was_held = False

def pressed():
    print("button was pressed not held")

if __name__ == '__main__':
    print ('running box')
    print ("Press button to lock (if unlocked), or unlock if the correct face is detected.")
    print ("Press Ctrl-C to quit.")
    green = LED(17)
    btn = Button(27)
    btn.was_held = False
    
    btn.when_held = held
    btn.when_released = released

    while True:
        green.on()
        print('green on')
        time.sleep(5)
        green.off()
        print('green off')
        time.sleep(5)