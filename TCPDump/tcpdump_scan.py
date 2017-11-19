#!/usr/bin/python

import subprocess

def tcpdump_scan_function():
        path = '/home/pi/Shuriken/Tools/RASPY_HACK_BOOT/TCPDump'
        print "[$ Shuriken $] Executing > tcpdump"
        option = raw_input('[$ Shuriken $] Executing with options ? ("y" or "n") >')
        if "y" in option:
            name_pcap = raw_input('[$ Shuriken $] Name of .pcap file >')
            nmap_Path = str("TCPDump/Captures/" + name_pcap + ".pcap")
            size_captura = raw_input('[$ Shuriken $] Number of packages of capture >')
            args = str('-c ' + size_captura + ' -w ' + nmap_Path + ' -vv &')
            comand = str('tcpdump ' + args)
            print "[$ Shuriken $] Args > " + args
            subprocess.call(comand, shell=True)
        elif "n" in option:
            process = subprocess.Popen(['tcpdump', '-vvv'], stdout=subprocess.PIPE)
            for row in iter(process.stdout.readline, b''):
                print row.rstrip()