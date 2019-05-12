#!/usr/bin/python

from sys import argv
import subprocess

def help():
    print "----------- HELP -----------"
    print " - help        : this Shiet"
    print " - mode        : Only two options"
    print "               :   - mode sniff"
    print "               :   - mode fakeAP"
    print " - mode sniff  : Use -mode sniff <wireless-interface> <folder-to-record>"
    print " - mode fakeAP : Use -mode fakeAP "

def sniff(interface, filename):
    print("[*] Init sniff mode ...")

    # Command Example : airodump-ng wlan0 -w wlan_0 --output-format csv
    pathFile = "/home/pi/Shuriken/Wlan_Gathering/" + str(filename)
    comand = "airodump-ng " + str(interface) + " -w " + str(pathFile) + " --output-format csv"
    cm = 'screen -S pySniff -p 0 -X stuff "' + str(comand) +'^M"'
    subprocess.call(cm, shell=True)


if __name__ == "__main__":
    if len(argv) <= 1:
        help()
    else:
        if str(argv[1]) == '-mode':
            if len(argv) >= 3:
                if str(argv[2]) == 'sniff':
                    if len(argv) >= 5:
                        print("[*] Mode Sniffing enable")
                        sniff(str(argv[3]), str(argv[4]))
                    else:
                        print("[-] Use -mode snif <wireless-interface> <filename-to-record>")
                elif str(argv[2]) == 'fakeAP':
                    print("[*] Mode Fake AP enable")
            else:
                print("[-] Use -mode <sniff> or <fakeAP>")
                print "[-] Use -help to know how to use"
        elif str(argv[1]) == '-help':
            help()
        else:
            help()