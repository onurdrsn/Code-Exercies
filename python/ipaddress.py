#!usr/bin/env python

import socket
hostname = socket.gethostname()
Ip= socket.gethostbyname(hostname)
print(f"My IP ADDRESS is: {Ip}\n")
