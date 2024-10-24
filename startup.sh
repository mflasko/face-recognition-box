#!/bin/bash

# to make exexcutable: chmod +x startup.sh
# to run it on each pi boot: 
# sudo crontab -e
# @reboot /home/flasko/github/face-recognition-box/startup.sh

echo "box startup script started"
# start the alternate pin factory daemon
sudo pigpiod
# active python virtual env
source /home/flasko/python/wsm/bin/activate

echo "starting box program"
python /home/flasko/github/face-recognition-box/box.py


