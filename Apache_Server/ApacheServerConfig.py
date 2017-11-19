#!/usr/bin/python

import subprocess
import sys

def START_apache():
    print "[$ Shuriken $] Executing > service apache2 start"
    subprocess.call('service apache2 start', shell=True)

def STOP_apache():
    print "[$ Shuriken $] Executing > service apache2 stop"
    subprocess.call('service apache2 stop', shell=True)

def back():
    print "[$ Apache $] Back  \n"

options = {'0': back, '1': START_apache, '2': STOP_apache}

def apacheMenu():
    print "\n"
    print "                       - Nmap Options -"
    print ""
    print "               0 : Back"
    print "               1 : START apache server"
    print "               2 : STOP apache server"
    print "\n"
    n = raw_input('[$ Apache $] > ')
    options[n]()