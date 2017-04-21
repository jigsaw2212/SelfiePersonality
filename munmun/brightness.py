import PIL
import Image
import math
import numpy as np 

im = Image.open("test.jpg")

arr = []

def get_brightness(r,g,b):
	return math.sqrt(0.299*r*r + 0.587*g*g + 0.114*b*b)     #brightness  =  sqrt( .299 R2 + .587 G2 + .114 B2 )
															#http://alienryderflex.com/hsp.html

print im.getpixel((0,0))
x,y = im.size

count = 0

for p in range((x)):
	for q in range((y)):
		temp = im.getpixel((p,q))
		r,g,b =  temp
		brightness = get_brightness(r,g,b)
		# print brightness
		arr.append(brightness)
		# print arr
		count += 1
		print count

print np.mean(arr)
print np.median(arr)

