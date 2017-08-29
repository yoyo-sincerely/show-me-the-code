#!/usr/bin/python3
# -*- coding:utf8 -*-

'''
网页上的超链接一般分为三种：一种是绝对URL的超链接。URL（Uniform Resource Locator）就是统一资源定位符，简单地讲就是网络上的一个站点、网页的完整路径。
第二种是相对URL的超链接。如将自己网页上的某一段文字或某标题链接到同一网站的其他网页上面去；
还有一种称为同一网页的超链接，这种超链接又叫做书签。

<a></a><!--一个超级链接。-->
<a title="百度百科"></a><!--一个有标题的超链接。-->
<a href="mailto"></a><!--一个自动发送电子邮件的链接。-->
锚点链接
<a href="#百度百科"></a><!--一个有标题的超链接。-->
'''

import codecs
import os, re
import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# FILE_PATH = 'page\\page.html'
URL = 'http://www.ruanyifeng.com/blog/2015/05/co.html'

def getUrl(url):
    requst = urllib.request.urlopen(url)
    return requst

def analizeCode(filename):
    # print(filename)
    # 获取协议，域名
    o = urlparse(URL)
    proto = o.scheme
    domain = o.netloc
    # print(o.geturl())
    # 提取超链接
    soup = BeautifulSoup(filename, "html.parser")
    # 过滤
    # for link in soup.find_all('a'):
    #     print(link.get('href'))
    a = soup.find_all('a')
    alist = [i.attrs['href'] for i in a if i.attrs['href'][0] != 'j']
    # 将形如#comment-text的锚点补全成http://www.ruanyifeng.com/blog/2015/05/co.html,将形如/feed.html补全为http://www.ruanyifeng.com/feed.html
    # alist = map(lambda i: proto + '://' + domain + i if i[0] == '/' else url + i if i[0] == '#' else i, alist)
    List = []
    for i in alist:
        if i[0] == '/':
            i = proto + '://' + domain + i
        elif i[0] == '#':
            i =  o.geturl()
        else :
            i = i
        List.append(i)
    return List


if __name__ == '__main__':
    for i in analizeCode(getUrl(URL)):
        print(i)
    