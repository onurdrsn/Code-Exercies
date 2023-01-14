# pip3 install pyqrcode
# pip3 install pypng

import pyqrcode
from pyqrcode import QRCode
import png 

url = pyqrcode.create("Your String or url")
url.png('qr3.png', scale=8)
