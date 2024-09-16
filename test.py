import time
from gpiozero import Button, LED

global tp

if __name__ == '__main__':
    print ('running box')
    print ("Press button to lock (if unlocked), or unlock if the correct face is detected.")
    print ("Press Ctrl-C to quit.")
    green = LED(27)

    while True:
        green.on()
        print('green on')
        time.sleep(5)
        green.off()
        time.sleep(5)
        print('green off')

        
        