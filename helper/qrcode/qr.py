import pyqrcode as qr
from PIL import Image as i

link = "https://github.com/gatilhoroxo"
qr_code = qr.create(link)
qr_code.png("QRCode.png",scale = 5)
i.open("QRCode.png")

