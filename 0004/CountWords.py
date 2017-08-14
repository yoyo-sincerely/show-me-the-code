#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
任一个英文的纯文本文件，统计其中的单词出现的个数。
'''

import re,sys,os
path = os.path.split(os.path.realpath(__file__))[0]
Fliter = re.compile("[^A-Za-z-\']|((?<![A-Za-z])[-\'])|([-\'](?![A-Za-z]))")
Divider = re.compile("\s")
File = open(path+"\input.txt").read()
Data =  Divider.split(Fliter.sub(" ",File))
Dict = {}
for i in Data:
	j = i.lower()
	try:
		Dict[j]+=1
	except KeyError:
		Dict[j] =1
	except:
		raise
for i in  Dict.items():
	print ("%s:%s"%i)

# import re
#
# pattern = 'this'
# text = 'Does this text match the pattern?'
#
# match = re.search(pattern, text)
#
# s = match.start()
# e = match.end()
#
# print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(
#     match.re.pattern, match.string, s, e, text[s:e]))