# -*- coding: UTF-8 -*-
import os
from PIL import Image

def transfer(img_path,dst_width,dst_height,dst_path):
	im = Image.open(img_path)
	s_w,s_h = im.size
	print("输出图像宽和高:  {} , {}".format(s_w, s_h))
	if dst_width/s_w < dst_height/s_h:
		ratio = dst_width/s_w
	else:
		ratio = dst_height/s_h
	print("图像缩放比例：{} ".format(ratio))
	resized_img = im.resize((int(ratio*s_w), int(ratio*s_h)), Image.ANTIALIAS)
	s_w,s_h = resized_img.size
	print("输出处理好的图像宽和高:  {} , {}".format(s_w, s_h))
	print()
	resized_img.save(dst_path)

if __name__ == '__main__':
	path = os.path.split(os.path.realpath(__file__))[0]+"\\"
	src = "img\\"
	dst = "finish_img\\"
	imgs = os.listdir(path+src)

	# for i in imgs:
	# 	print(i)
	for i in imgs:
		transfer(path+src+i,1136,640,path+dst+i)