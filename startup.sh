#!/bin/bash

echo "box startup script started"
# start the alternate pin factory daemon
sudo pigpiod
# active python virtual env
source /home/flasko/python/wsm/bin/activate

echo "starting box program"
python box.py


