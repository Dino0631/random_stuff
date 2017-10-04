try:
	import sys
	import os
	import PIL
	from PIL import Image, ImageDraw
	imagewidth = 500
	imageheight = 500
	PATH = os.path.join('data')
	IMAGE = os.path.join(PATH, 'image.png')
	IMAGE = 'data/image.png'
	try:
		img = Image.open(IMAGE)
	except FileNotFoundError:
		img = Image.new('RGB', (imagewidth, imageheight))
	print('hi')
	draw  = ImageDraw.Draw(img, mode='RGB')
	draw.ellipse([(100,100),(200,200)])
	img.save("PNG")


except Exception as e:
	print(e)
input()