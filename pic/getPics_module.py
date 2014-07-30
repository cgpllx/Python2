# coding=utf-8
# Filename:getPics_module.py
# 获取美女图片网站的数据

import socket
import urllib2
import urllib
import re
import time
import random

def getHtml(url):
	# timeout = 40
	request = urllib2.urlopen(url)
	html = request.read()
	request.close()
	return html
	
def getHtml3(url):
	# content = ''
	proxys = [{'http':'183.207.229.146:80'},{'http':'58.254.132.87:80'},{'http':'14.29.117.38:8081'}]
	i = random.randint(0,len(proxys)-1)
	proxy = proxys[i]
	
	proxy_support = urllib2.ProxyHandler(proxy) 
	opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
	urllib2.install_opener(opener)
	content = urllib2.urlopen(url).read()
	
	return content

# 获取HTML代码
def getHtml2(url):
	req_header = {'Host':'www.meinv369.com',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
	'Accept-Encoding':'gzip, deflate',
	'Cookie':'AJSTAT_ok_times=2; AJSTAT_ok_pages=1',
	'Connection':'keep-alive',	
	'Cache-Control':'max-age=0',
	'Referer':'www.meinv369.com' #注意如果依然不能抓取的话，这里可以设置抓取网站的host
	}
	req_timeout = 80
	sleep_download_time = 3
	time.sleep(sleep_download_time)
	req = urllib2.Request(url,None,req_header)
	resp = urllib2.urlopen(req,None,req_timeout)
	html = resp.read()
	resp.close()
	return html
	
# 存储html代码
def saveHtml(html,filename):
	f = file(filename,'wb')
	f.write(html)
	f.close()

# 获取网站栏目
def getTopic(pattern,html):
	p = re.compile(pattern,re.DOTALL)
	html2 = p.findall(html)
	# print html2[0]
	# exit()
	p2 = re.compile(r"<a href=['\"](.*?)['\"][^>]*?>(.*?)</a>",re.DOTALL)
	data = p2.findall(html2[0])
	# print data
	return data
	
# 获取href
def getHref(html):
	p = re.compile(r"<a href=['\"](.*?)['\"][^>]*?>(.*?)</a>",re.DOTALL)
	data = p.findall(html)
	# print data
	return data
	
# 获取图片URL
def getPic(html):
	p_src = re.compile(r"img src=['\"](.*?)['\"][^>]*?/>")
	srcs = p_src.findall(html)
	# print srcs[0]
	return srcs[0]
	
# 获取图集和图集标题、图集封面URL、图集URL
def getAlbum(html):
	p_href = re.compile(r"<a[^>]*?href=['\"](.*?)['\"][^>]*?>")
	hrefs = p_href.findall(html)
	
	p_src = re.compile(r"img src=['\"](.*?)['\"][^>]*?/>")
	srcs = p_src.findall(html)
	
	p_title = re.compile(r"<p>(.*?)</p>")
	titles = p_title.findall(html)
	
	num = len(hrefs)
	res = []
	
	for i in range(num):
		album = {'album_title':titles[i],'album_thumb_net':srcs[i],'album_url':hrefs[i]}
		
		res.append(album)
	
	
	# print res
	return res

# 处理URLhttp://www.meinv369.com/sex/869.html，分离出http://www.meinv369.com/sex/869
def formatUrl(url):
	pos = url.find('.html',0)
	res = ''
	for i in range(pos):
		res = res + url[i]
	# print res
	return res

# 保存图片
def saveFile(path,url):
	data = urllib2.urlopen(url).read()
	f = file(path,"wb")
	f.write(data)
	f.close()
	
# 时间数
def nameTime():
	t = time.time()
	s = str(t)
	ss = s.split('.')
	name = ss[0] + ss[1]
	return name
	
# 获取图片名
def getPicName(url):
	arr = url.split('/')
	name = arr[-1]
	name = nameTime() + name
	return name
	
	# print hrefs[0]
	# print srcs[0]
	# print titles[0]