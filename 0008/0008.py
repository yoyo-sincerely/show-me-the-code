#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import os, sys

path = os.path.split(os.path.realpath(__file__))[0] + "\\text.txt"

def Soup(html):
	soup = BeautifulSoup(html, "html.parser")
	return soup.text

def getText():
	r = requests.get("http://www.wuxiaworld.com/col-index/col-volume-1-chapter-1/")
	return r.text

if __name__ == '__main__':
	f = open(path, "wb")
	text = getText()
	# print(type(text))
	f.write(Soup(text).encode('utf8').strip())
	f.close()
