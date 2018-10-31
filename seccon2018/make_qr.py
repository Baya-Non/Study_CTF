import qrcode
from PIL import Image 
img = qrcode.make('Thank you. \n I am looking forward to the write up of SECCON2018 ):')
#img.show()
img.save('sample2.png')

