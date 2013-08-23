#!/usr/bin/python
import os
from PIL import Image
f = open("gencss.css","w")
def generatecss(img):
	fimg = Image.open(img)
	width, height = fimg.size
	css = img[:-4] + "{\n\tbackground:url('"+ img +"');\n\twidht:" + str(width) + "px;\n\theight:"+str(height)+"px;\n\t}\n"
	return css
for dirname, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith(".png") or filename.endswith(".gif") or filename.endswith(".jpg") or filename.endswith(".PNG") or filename.endswith(".GIF") or filename.endswith(".JPG"):
        	f.write(generatecss(filename))