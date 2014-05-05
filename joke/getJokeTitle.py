# encoding:utf8
# Filename: getJokeTitle.py
# get http://www.jokeji.cn/list29_1.htm joke title url and page number

import re
import urllib2

def getHtml(url):
	try:
		html = urllib2.urlopen(url).read()
		return html
	except:
		pass

def getPageNum(html):
	pattern = re.compile(r'',re.DOTALL)
	match = pattern.findall(pattern)
	return match

def getPageDiv(html):
	pattern = re.compile(r'',re.DOTALL)
	match = pattern.findall(pattern)
	return match