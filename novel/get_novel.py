# coding=utf-8
# 采集http://www.177tvb.com/files/article/html/56/56027/index.html小说

import time
import re
import urllib2
import cPickle as p
from MyDB import MyDB

# 从序列化存储文件中读取数据
def read_data(filename):
	f = file(filename)
	data = p.load(f)
	return data

# 序列化保存数据
def save_data(data,filename):
	f = file(filename,'w')
	p.dump(data,f)
	f.close()

def get_html(url):
	html = urllib2.urlopen(url).read()
	return html
	
def save_html(data,filename,mode,i=1):
	f = file(filename,mode)
	f.write(data)
	if(i==1):
		f.write('\r\n')	
	f.close()

# get html from a filename
def read_html(filename):
	data = ''
	f = file(filename)
	while True:
		line = f.readline()
		# print line
		if len(line) == 0:
			break;
		data += line
	return data
	
def get_novel_list(html):
	pattern = re.compile('<div class="readerListShow">(.*?)</div>',re.DOTALL)
	res = pattern.findall(html)
	return res
	# print res
	
def get_chapter_title2(html):
	data = {}
	pattern = re.compile('<a href="(.*?)">(.*?)</a>',re.DOTALL)
	res = pattern.findall(html)
	for r in res:
		data[r[0]] = r[1]
	# return res
	# print res
	return data
	
def get_chapter_title(html):
	pattern = re.compile('<a href="(.*?)">(.*?)</a>',re.DOTALL)
	res = pattern.findall(html)	
	return res

# 存储章节数据到数据库	
def save_chapters():
	# html = read_html('b.txt')
	url = 'http://www.177tvb.com/files/article/html/16/16870/index.html'
	html = get_html(url)

	novel_list = get_novel_list(html)
	# print novel_list

	chapter_titles = get_chapter_title(novel_list[0])
	for i in chapter_titles:
		# print i + '-----' + j
		# print i[1]
		# save_html(i[0] + '----' + i[1],'aa.txt','ab')
		# continue
		
		pre = 'http://www.177tvb.com/files/article/html/16/16870/'
		book_id = 2
		chapter_title = i[1]
		chapter_url = pre + i[0]
		print chapter_url + '---------' + chapter_title
		s = chapter_title.decode('gbk')
		# print s
		u = s.encode('utf8')
		# print u
		# continue
		db.saveChapter(book_id,u,chapter_url)
	else:
		print 'done'
		
# 获取小说正文内容
def get_content(html):
	pattern = re.compile('<div id="content">(.*?)</div>',re.DOTALL)
	data = pattern.findall(html)
	# print data[0]
	return data[0]

# 小说正文
def save_content():
	counter = 0
	# url = 'http://www.177tvb.com/files/article/html/56/56027/10017499.html'
	tip = '你想采集多少条？\n'
	s = tip.decode('utf8')
	tip = s.encode('gbk')
	n = int(raw_input(tip))
	datas = db.selectChapter(n)
	for data in datas:		
		# print data[3]
		if(counter==5):
			time.sleep(5)
			counter = 0
		url = data[3]
		html = get_html(url)
		content = get_content(html)
		chapter_id = data[0]
		s = content.decode('gbk')
		content_text = s.encode('utf8')
		# print s
		res = db.saveContent(chapter_id,content_text)
		if res == True:
			i = 1
			j = chapter_id
			db.setChapterIf(i,j)
			print 'gather ' + url + ' success'
			counter = counter + 1
		else:
			print 'gather ' + url + ' failure'
		
	exit()	
	
host = 'localhost'
root = 'root'
pwd = ''
db = 'novel'
chset = 'utf8'
db = MyDB(host,root,pwd,db,chset)

# save_content()
# html = read_html('content.txt')
# content = get_content(html)

# chapter_id = 1
# s = content.decode('gbk')
# content_text = s.encode('utf8')
# db.saveContent(chapter_id,content_text)

# save_chapters()


save_content()


