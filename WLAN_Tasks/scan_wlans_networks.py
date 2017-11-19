#!/usr/bin/python

import subprocess

def network_scan():
        print "[Shuriken] Executing > sudo iwlist wlan0 scan"
        subprocess.call('sudo iwlist wlan0 scan', shell=True)