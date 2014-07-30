# coding=utf-8
# 使用代理服务器
# filename:proxy.py

import random
import urllib2 
proxys = [{'http':'124.161.94.8:80'},{'http':'183.207.229.146:80'},{'http':'58.254.132.87:80'},{'http':'14.29.117.38:8081'},{'http':'125.219.11.53:1140'},{'http':'114.228.235.202:1138'}]
i = random.randint(0,len(proxys)-1)
# print i
proxy = proxys[i]
print proxy
proxy_support = urllib2.ProxyHandler(proxy) 
opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
urllib2.install_opener(opener) 
content = urllib2.urlopen('http://www.ifeng.com').read()
# print content
print content


