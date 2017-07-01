#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
'''

import pymysql, os, re

path = os.path.split(os.path.realpath(__file__))[0] + "\code.txt"
f = open(path, "r")
A = f.read()
arr = re.split("\s+", A)
# print(len(arr[55]))

# 打开数据库连接
db = pymysql.connect("localhost","root","yoyo331200","TEST" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print ("Database version : %s " % data)

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS CODE")
sql = """CREATE TABLE CODE (
         no INT,
		  content text
		 )"""
cursor.execute(sql)

for i in range(len(arr)):
    # print(i,arr[i])
    sql = """INSERT INTO CODE VALUES (%d, "%s")""" % (i, arr[i])
    # print(sql)
    cursor.execute(sql)
    db.commit()

# 关闭数据库连接
db.close()