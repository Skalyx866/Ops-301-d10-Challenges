#!/bin/python

# import OS library
import os

whoami = os.system("whoami")
ipaddress = os.system("ip a")
hardware = os.system("lshw -short")

def mainfunction():
        
        print(whoami)
        print(ipaddress)
        print(hardware)
        
mainfunction()