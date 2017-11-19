#!/usr/bin/python

import subprocess
import sys

def basic_scan():
    print "[$ Shuriken $] Executing > nmap -sT -Pn"
    option = raw_input('[$ Shuriken $] Save results ? ("y" or "n") >')
    if "y" in option:
        result = raw_input('[$ Shuriken $] Name of result file >')
        nmap_Path = str("Nmap/Results/" + result + ".xml")
        target_ip = raw_input('[$ Shuriken $] Target IP >')
        args = str('-sT -Pn ' + target_ip + ' -oN ' + nmap_Path )
        comand = str('nmap ' + args)
        print "[$ Shuriken $] Args > " + args
        subprocess.call(comand, shell=True)
    elif "n" in option:
        target_ip = raw_input('[$ Shuriken $] Target IP >')
        args = str('-sT -Pn ' + target_ip)
        comand = str('nmap ' + args)
        print "[$ Shuriken $] Args > " + args
        subprocess.call(comand, shell=True)

def hard_scan():
    print "[$ Shuriken $] Executing > nmap -sS -A -O -sV"
    option = raw_input('[$ Shuriken $] Save results ? ("y" or "n") >')
    if "y" in option:
        result = raw_input('[$ Shuriken $] Name of result file >')
        nmap_Path = str("Nmap/Results/" + result + ".xml")
        target_ip = raw_input('[$ Shuriken $] Target IP >')
        args = str('-sS -A -O -sV ' + target_ip + ' -oN ' + nmap_Path)
        comand = str('nmap ' + args)
        print "[$ Shuriken $] Args > " + args
        subprocess.call(comand, shell=True)
    elif "n" in option:
        target_ip = raw_input('[$ Shuriken $] Target IP >')
        args = str('-sS -A -O -sV ' + target_ip)
        comand = str('nmap ' + args)
        print "[$ Shuriken $] Args > " + args
        subprocess.call(comand, shell=True)

def evade_ids_scan():
    print "[$ Shuriken $] Executing > nmap --spoof-mac Cisco -T4 --source-port 53 -sS --send-ip -n --data-length 30 --randomize-hosts -n -f -sV --version-all -O"
    option = raw_input('[$ Shuriken $] Save results ? ("y" or "n") >')
    if "y" in option:
        result = raw_input('[$ Shuriken $] Name of result file >')
        nmap_Path = str("Nmap/Results/" + result + ".xml")
        target_ip = raw_input('[$ Shuriken $] Target IP >')
        args = str('--spoof-mac Cisco -T4 --source-port 53 -sS --send-ip -n --data-length 30 --randomize-hosts -n -f -sV --version-all -O ' + target_ip + ' -oN ' + nmap_Path)
        comand = str('nmap ' + args)
        print "[$ Shuriken $] Args > " + args
        subprocess.call(comand, shell=True)
    elif "n" in option:
        target_ip = raw_input('[$ Shuriken $] Target IP >')
        args = str('--spoof-mac Cisco -T4 --source-port 53 -sS --send-ip -n --data-length 30 --randomize-hosts -n -f -sV --version-all -O ' + target_ip)
        comand = str('nmap ' + args)
        print "[$ Shuriken $] Args > " + args
        subprocess.call(comand, shell=True)

def back():
    print "[$ nmap $] Back  \n"

options = {'0': back, '1': basic_scan, '2': hard_scan, '3': evade_ids_scan}

def nmapMenu():
    print "\n"
    print "                       - Nmap Options -"
    print ""
    print "               0 : Back"
    print "               1 : Basic scan"
    print "               2 : Hard scan"
    print "               3 : Evade Ids scan"
    print "\n"
    n = raw_input('[$ nmap $] > ')
    options[n]()
