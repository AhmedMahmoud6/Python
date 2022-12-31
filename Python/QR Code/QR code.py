import pyqrcode

s = "https://cdn.discordapp.com/attachments/953719840210812980/1051225727527292948/318992293_1157476371540323_7261867801677749891_n.jpg"
url = pyqrcode.create(s)
url.svg("myqr.svg", scale=8)
url.png("myqr.png", scale=6)
