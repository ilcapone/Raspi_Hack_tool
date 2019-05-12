#!/usr/bin/python

import sys

from Nmap import nmap_Scaner
from WLAN_Tasks import scan_wlans_networks
from TCPDump import tcpdump_scan
from ArpSpoofing import arpSpoofing
from BruteForceRouter import bruteForceRouterDiccionary
from Apache_Server import ApacheServerConfig

def MEDIARECORD():
    print"[$ Shuriken $] Init Media Record config menu ..."

def APACHESERVER():
    print"[$ Shuriken $] Init Apache Server config menu ..."
    ApacheServerConfig.apacheMenu()

def BRUTEFORCE_ROUTERLOGIN():
    print"[$ Shuriken $] Under Construccion ..."
    #print"[$ Shuriken $] Init brute force versus the router login ..."
    #bruteForceRouterDiccionary.init_BruteForceRouert()

def ARPSPOOGING():
    print"[$ Shuriken $] Init arp spoofing function ..."
    target_ip = raw_input('[$ Shuriken $] Insert target victim IP> ')
    gateway_ip = raw_input('[$ Shuriken $] Insert Gateway IP > ')
    arpSpoofing.exe_arpSpoofing(target_ip, gateway_ip)

def Tcpdump_Scan():
    print"[$ Shuriken $] Init tcpdump scan function ..."
    tcpdump_scan.tcpdump_scan_function()

def Wlan_Scan_use():
    print"[$ Shuriken $] Init scan wlan network function ..."
    scan_wlans_networks.network_scan()

def Nmap_use():
    print"[$ Shuriken $] Init scan network function ..."
    nmap_Scaner.nmapMenu()

def exit():
    print "[$ Shuriken $] Exit \n"
    sys.exit()

options = {'0': exit, '1': Nmap_use, '2': Wlan_Scan_use, '3': Tcpdump_Scan, '4': ARPSPOOGING, '5': BRUTEFORCE_ROUTERLOGIN, '6': APACHESERVER, '7': MEDIARECORD}

def MenuLocal():
    while True:
        print "\n"
        print "                       - Raspy Options -"
        print ""
        print "               0 : Exit"
        print "               1 : Nmap"
        print "               2 : Wlan Scan Network"
        print "               3 : Tcpdump"
        print "               4 : ArpSpoofing"
        print "               5 : Brute Force Roueter Login"
        print "               6 : Apache Server"
        print "               7 : Media Record"
        print "\n"
        try:
            inp = raw_input('[$ Shuriken $] > ')
            n = str(inp)
            if '0' in n or '1' in n or '2' in n or '3' in n or '4' in n or '5' in n or '6' in n or '7' in n:
                options[n]()
            else:
                print('[$ Shuriken $] Is not recognized as a valid command')
        except KeyboardInterrupt:
            print "Stopping Shuriken"
            sys.exit()

if __name__ == "__main__":
    MenuLocal()