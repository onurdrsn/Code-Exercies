#!/usr/bin/env python3
from os import execv
import pyfiglet
import socket
import sys
import subprocess


subprocess.call('clear', shell=True)

print(pyfiglet.figlet_format("PORT SCANNER"))

site = input("Hedef: ")

print("-" * 50)
print(f"Hedef Taraniyor: {socket.gethostbyname(site)}")
print("-" * 50)

try:
    for port in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        if sock.connect_ex((socket.gethostbyname(site), port)) == 0:
            print(f"Portunuz {format(port)}: Açik")
            
        sock.close()
    print("-" * 50)

except Exception as e:
    print("Hata!", e)

except KeyboardInterrupt:
    print("Ctrl+C presledin")
    sys.exit()

except EOFError:
    print("Hata: Girilen değer yok veya dosya sonlandirildi!")
    sys.exit()

except socket.gaierror:
    print("Ana bilgisayar adi çözülemedi. Çikiliyor...")
    sys.exit()

except socket.error:
    print("Sunucuya bağlanilamadi...")
    sys.exit()
