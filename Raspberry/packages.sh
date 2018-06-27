#!/usr/bin/env bash

sudo /usr/bin/apt-get update
sudo /usr/bin/apt-get upgrade -y
sudo /usr/bin/apt-get install python3 -y
sudo /usr/bin/apt-get install git -y
pip install numpy
pip install scipy
pip install imutils
pip install pyglet
pip install serial
pip install cv2
