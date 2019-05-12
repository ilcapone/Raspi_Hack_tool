#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -r 1280x720 --no-banner /home/pi/Shuriken/Tools/Raspi_Hack_tool/WebCam/Pictures/shot_$DATE.jpg
