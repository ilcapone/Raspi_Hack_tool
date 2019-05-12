#!/usr/bin/python

import subprocess
import sys

def START_apache():
    print "[$ Shuriken $] Executing > service apache2 start"
    subprocess.call('systemctl start apache2', shell=True)

def STOP_apache():
    print "[$ Shuriken $] Executing > service apache2 stop"
    subprocess.call('systemctl stop apache2', shell=True)

def STATUS_apache():
    print "[$ Shuriken $] Executing > service apache2 stop"
    subprocess.call('systemctl status apache2', shell=True)

def back():
    print "[$ Apache $] Back  \n"

options = {'0': back, '1': START_apache, '2': STOP_apache, '3':STATUS_apache}

def apacheMenu():
    print "\n"
    print "                       - Apache Server Options -"
    print ""
    print "               0 : Back"
    print "               1 : START apache server"
    print "               2 : STOP apache server"
    print "               3 : STATUS apache server"
    print "\n"
    n = raw_input('[$ Apache $] > ')
    options[n]()