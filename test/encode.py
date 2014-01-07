import base64
import urllib

image = urllib.urlopen("https://raw.github.com/defm03/qtb64id/master/res/encodedb64.jpg")
image64 = base64.encodestring(image.read())
txtfile = open("todecode.txt", "w")
txtfile.write(image64)
txtfile.close()
