import pyqrcode
from pyqrcode import QRCode
import png 

Qrstring = "qr.jpg"

url = pyqrcode.create(Qrstring)
url.png('Desktop/qr2.png', scale=8)
