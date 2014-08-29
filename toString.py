# -*- coding: utf-8 -*- 
from PIL import Image,ImageEnhance,ImageFilter,ImageDraw
import sys
import pyocr
import pyocr.builders
def to_string(im):
	#im=Image.open('1.tif')
	#im.convert('L')
	tools = pyocr.get_available_tools()
	if len(tools) == 0:
		print("No OCR tool found")
		sys.exit(1)
	tool = tools[0]
	#print("Will use tool '%s'" % (tool.get_name()))
	# Ex: Will use tool 'tesseract'

	langs = tool.get_available_languages()
	#print("Available languages: %s" % ", ".join(langs))
	lang = langs[1]
	#print("Will use lang '%s'" % (lang))
	# Ex: Will use lang 'fra'

	txt = tool.image_to_string(im,
						   lang=lang,
						   builder=pyocr.builders.TextBuilder())
	#print txt 
	return txt
def getPixel(image,x,y,G,N):  
	L = image.getpixel((x,y))  
	if L > G:  
		L = True  
	else:  
		L = False  
  
	nearDots = 0  
	if L == (image.getpixel((x - 1,y - 1)) > G):  
		nearDots += 1  
	if L == (image.getpixel((x - 1,y)) > G):  
		nearDots += 1  
	if L == (image.getpixel((x - 1,y + 1)) > G):  
		nearDots += 1  
	if L == (image.getpixel((x,y - 1)) > G):  
		nearDots += 1  
	if L == (image.getpixel((x,y + 1)) > G):  
		nearDots += 1  
	if L == (image.getpixel((x + 1,y - 1)) > G):  
		nearDots += 1  
	if L == (image.getpixel((x + 1,y)) > G):  
		nearDots += 1  
	if L == (image.getpixel((x + 1,y + 1)) > G):  
		nearDots += 1  
  
	if nearDots < N:  
		return image.getpixel((x,y-1))  
	else:  
		return None  
  
# 降噪   
# 根据一个点A的RGB值，与周围的8个点的RBG值比较，设定一个值N（0 <N <8），当A的RGB值与周围8个点的RGB相等数小于N时，此点为噪点   
# G: Integer 图像二值化阀值   
# N: Integer 降噪率 0 <N <8   
# Z: Integer 降噪次数   
# 输出   
#  0：降噪成功   
#  1：降噪失败   
def clearNoise(image,G,N,Z):  
	draw = ImageDraw.Draw(image)  
  
	for i in xrange(0,Z):  
		for x in xrange(1,image.size[0] - 1):  
			for y in xrange(1,image.size[1] - 1):  
				color = getPixel(image,x,y,G,N)  
				if color != None:  
					draw.point((x,y),color)  
def toString(image):
	#image=Image.open('index (3).png')
	#image.convert('1')
	image = image.filter(ImageFilter.MaxFilter(1))
	enhancer = ImageEnhance.Contrast(image)
	image = enhancer.enhance(2)
	image = image.convert('L')
	clearNoise(image,8,2,2)
	#image.show()
	return to_string(image)
if __name__=='__main__':
	toString(Image.open('index (3).png'))
