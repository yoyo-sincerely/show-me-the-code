#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
'''
import os,time,random,hashlib

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

path = os.path.split(os.path.realpath(__file__))[0] + "\code.txt"

@log
def salt():
	return "%s"*5%tuple([random.randint(10000000,99999999) for i in range(5)])

@log
def md(str):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()

res = [md(salt() + str(time.time())) for i in range(200)]
f = open(path, "w")
for i in res:
    f.write(i+"\n")
f.close()