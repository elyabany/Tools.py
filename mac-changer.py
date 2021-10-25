#!/usr/bin/env python
import subprocess #to access command 
import optparse

#ex. 

#parser to handle user input using args 
def get_arguments():
    parser =optparse.OptionParser()
    parser.add_option("-i","--interface" , dest="interface" , help=" Your Interface")
    parser.add_option("-m","--mac" , dest="mac" , help=" enter new mac address")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        #code to handle error 
        parser.error("[-] please enter an interface , use --help for info ")

    elif not options.mac:
        #code to handler error 
        parser.error("[-] please enter a new mac address  , use --help for info ")
    return options



def change_mac(interface,mac):
       #user input 
    print ("[+] changing MAC address for --> "+interface)
    print ("[+] changinh MAC address to --> "+mac)

   #run the commands 
    subprocess.call([" ifconfig" , interface , "down"])
    subprocess.call([" ifconfig" , interface , "hw ","ether", mac])
    subprocess.call([" ifconfig" , interface , "up"])


options=get_arguments()
change_mac(options.interface , options.mac)
