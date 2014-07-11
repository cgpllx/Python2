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
	pattern = re.compile(r'<div.*?class="next_page">(.*?)</div>',re.DOTALL)
	match = pattern.findall(html)
	# print match[0]
	return match[0]

def getPageDiv(html):
	pattern = re.compile(r'<a.*?href="list\d{0,}_(\d{0,})[^>]*?">',re.DOTALL)
	match = pattern.findall(html)
	# print match[-1]
	return match
	
def getListTitle(html):
	pattern = re.compile(r'<div.*?class="list_title">(.*?)</div>',re.DOTALL)
	match = pattern.findall(html)
	# print match[0]
	return match[0]

def getTitleUrl(html):
	pattern = re.compile(r'<a.*?href="(.*?)"[^>]+?>(.*?)</a>',re.DOTALL)
	match = pattern.findall(html)
	# print match[0][0]
	# print match[0][1]
	return match

def getJokeContent(html):
	pattern = re.compile(r'<span id="text110">(.*?)</span>',re.DOTALL)
	match = pattern.findall(html)
	print match[0]
	return match
	
# test
# url = 'http://www.jokeji.cn/list29_1.htm'
url = 'http://www.jokeji.cn/list4_1.htm'
html = getHtml(url)



pageName = getPageNum(html)
pageDiv = getPageDiv(pageName)

# get title
listTitle = getListTitle(html)
titleUrl = getTitleUrl(listTitle)
for t in titleUrl:
	# print t[0]
	print t[1]

# get content
url = 'http://www.jokeji.cn/jokehtml/jt/2014040600035154.htm'
html = getHtml(url)
# save html
f = file('joke.txt','w')
f.write(html)
f.close()
jokeContent= getJokeContent(html);
print jokeContent[0]
