import time
from gpiozero import Button, LED, Servo
import gpiod
global tp

if __name__ == '__main__':
    print ('running box')
    print ("Press button to lock (if unlocked), or unlock if the correct face is detected.")
    print ("Press Ctrl-C to quit.")
    green = LED(22)
    
    LED_PIN = 17
    chip = gpiod.Chip('gpiochip4')
    led_line = chip.get_line(LED_PIN)
    led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
    led_line.set_value(1)	

    print('set value of gpio 17 . sleep for 10 sec')
    time.sleep(10)

    while True:
        green.on()
        print('green on')
        time.sleep(3)
        green.off()
        print('green off')

        
        