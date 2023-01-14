#!usr/bin/env python
#pip3 install WhatIsMyIP

#find ip address in three different ways

import socket

print(f"My Local Ip is: {socket.gethostbyname(socket.gethostname())}\n")


import whatismyip

print(f"Public Ipv4: {whatismyip.whatismyipv4()}\nPublic Ipv6: {whatismyip.whatismyipv6()}\n")


from urllib.request import urlopen
import re as r
 
def getIP():
    return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(str(urlopen('http://checkip.dyndns.com/').read())).group(1)
 
print(f"Your Ipv4: {getIP()}")
