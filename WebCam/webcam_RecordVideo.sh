#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

ffmpeg -f v4l2 -r 25 -s 640x480 -i /dev/video0  /home/pi/Shuriken/Tools/Raspi_Hack_tool/WebCam/Videos/videoSHOT__$DATE.avi
