# -*- coding:utf-8 -*-
import os
from os.path import join
from PIL import Image

cwd = os.getcwd()

def resizeIcon(verName, verSize):
	img = Image.open(join(cwd,"source.png"))
	if verSize[0] <= img.size[0]:
		sampleOpt = Image.ANTIALIAS
	else:
		sampleOpt = Image.BILINEAR
	newImg = img.resize(verSize, sampleOpt)
	newImg.save(join(cwd,verName));
	print("Done! "+verName+" width:"+str(newImg.size[0])+" height:"+str(newImg.size[1]))

resizeIcon("Icon.png", (57,57))
resizeIcon("Icon@2x.png", (114,114))
resizeIcon("Icon-60@2x.png", (120,120))
resizeIcon("Icon-72.png", (72,72))
resizeIcon("Icon-72@2x.png", (144,144))
resizeIcon("Icon-76.png", (76,76))
resizeIcon("Icon-76@2x.png", (152,152))
resizeIcon("Icon-Small.png", (29,29))
resizeIcon("Icon-Small@2x.png", (58,58))
resizeIcon("Icon-Small-40.png", (40,40))
resizeIcon("Icon-Small-40@2x.png", (80,80))
resizeIcon("Icon-Small-50.png", (50,50))
resizeIcon("Icon-Small-50@2x.png", (100,100))

