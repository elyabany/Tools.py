#!/usr/bin/env python
import subprocess #to access command 
import optparse



#parser to handle user input using args 
parser =optparse.OptionParser()
parser.add_option("-i","--interface" , dest="interface" , help=" Your Interface")
parser.add_option("-m","--mac" , dest="mac" , help=" enter new mac address")

(options,arguments) = parser.parse_args()


def change_mac(interface,mac):
       #user input 
    print ("[+] changing MAC address for --> "+interface)
    print ("[+] changinh MAC address to --> "+mac)

   #run the commands 
    subprocess.call([" ifconfig" , interface , "down"])
    subprocess.call([" ifconfig" , interface , "hw ","ether", mac])
    subprocess.call([" ifconfig" , interface , "up"])

change_mac(options.interface , options.mac)