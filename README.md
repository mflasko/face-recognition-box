Raspberry Pi Face Recognition Treasure Box
==========================================

Raspberry Pi powered box which uses face recognition with OpenCV to lock and unlock itself.  See the tutorial [on the Adafruit learning system](http://learn.adafruit.com/raspberry-pi-face-recognition-treasure-box/overview).


For the IMX519 Camera to work made these changes: 
sudo nano /boot/firmware/config.txt 
#Find the line: [all], add the following item under it:
dtoverlay=imx519




Raspberry pi setup: 

1) RaspberryPiBox - credentials in app 
2) Run commands to setup a fresh PI: 

sudo apt update
sudo upt upgrade
sudo apt install python3-gpiozero
mkdir github
mkdir python
cd github
git clone https://github.com/mflasko/face-recognition-box.git
cd ../python
python3 -m venv wsm --system-site-packages


