# coding=utf-8
# 采集时仍然遭遇反采集限制，无法解决此问题，暂时不弄python采集了
# get picture from http://www.meinv369.com/
# Filename:get_pic_meinv369.py

from MyDB import MyDB
import getPics_module
import re
import time
import random



def saveTopics():
	url = 'http://www.meinv369.com/'
	html = getPics_module.getHtmlProxies(url)
	pattern_topic = '<div class="nav">(.*?)</div>'
	topics = getPics_module.getTopic(pattern_topic,html)
	# print topics
	for topic in topics:
		print topic[0] + '---' + topic[1]		
		topic_url = topic[0]
		s = topic[1].decode('gbk')
		topic_title = s.encode('utf8')
		# continue
		db.saveTopic(topic_title,topic_url)

# 获取图集列表部分的HTML		
def getPicsHtml(url):
	html = getPics_module.getHtmlProxies(url)
	# print html
	pattern = re.compile(r'<div class="i01">(.*?)</div>',re.DOTALL)
	res = pattern.findall(html)
	# print res[0]
	return res[0]
	

def saveAlbums():
	pre = 'http://www.meinv369.com'
	url = 'http://www.meinv369.com/mm/'
	topic_id = 9
	
	html = getPics_module.getHtmlProxies(url)
	pattern_page = re.compile(r'<div class="page page_l">(.*?)</div>',re.DOTALL)
	page_info = pattern_page.findall(html)
	print page_info[0]
	hrefs = getPics_module.getHref(page_info[0])	
	# print hrefs[len(hrefs)-1][0]
	pattern_page_num = re.compile(r'(list_\d*?_)(\d)*?\.html')
	page_num = pattern_page_num.findall(hrefs[len(hrefs)-1][0])
	# print page_num
	
	page_total = int(page_num[0][1])
	page_suffix = page_num[0][0]
	
	
	for i in range(page_total):
		print i
		album_url = url + page_suffix + str(i+1) + '.html'
		print album_url
		# exit()
		html_album = getPicsHtml(album_url)
		# print html_album
		albums_info = getPics_module.getAlbum(html_album)
		# print albums_info[0]
		# exit()
		for album in albums_info:			
			getOnePageAlbum(album_url,topic_id,pre)		
	exit()
	
# 获取一页图集列表的图集数据
def getOnePageAlbum(album_url,topic_id,pre):
	html_album = getPicsHtml(album_url)
	# print html_album
	# exit()
	albums_info = getPics_module.getAlbum(html_album)
	# print albums_info
	# exit()
	for album in albums_info:
		
		s = album['album_title'].decode('gbk')
		album_title = s.encode('utf8')
		album_thumb_net = pre + album['album_thumb_net']
		album_url = pre + album['album_url']
		
		print album_title
		print album_thumb_net
		print album_url
		db.saveAlbum(topic_id,album_title,album_thumb_net,album_url)

# 获取一个图集的所有图片
def getPhotos(url,pre,album_id):
	html = getPics_module.getHtmlProxies(url)
	pic = getPhoto(html)
	url = getPics_module.formatUrl(url)
	# print pic
	# exit()
	page_sum = getAlbumPage(html)
	# print page_sum
	# exit()
	# counter = 0
	for i in range(page_sum-1):
		url2 = url + '_' + str(i+2) + '.html'		
		html = getPics_module.getHtmlProxies(url2)
		pic = pre + '/' + getPhoto(html)
		print pic		
		res = db.savePicture(album_id,pic)
		if(res==False):
			db.saveAlbumPage(self,page,album_id)
		# counter += 1
		

# 获取大图URL
def getPhoto(html):	
	p_pic = re.compile(r'<div class="mypic">(.*?)</div>',re.DOTALL)
	srcs = p_pic.findall(html)	
	picture_net = getPics_module.getPic(srcs[0])
	return picture_net
	# db.saveAlbum(topic_id,album_title,album_thumb_net)

# 获取某个图集的图片页数
def getAlbumPage(html):
	p_page = re.compile(r'<div class="page page_c">(.*?)</div>',re.DOTALL)
	page_html = p_page.findall(html)
	# print page_html
	# exit()
	# 找出页码链接
	p_a = re.compile(r'<a[^>]*?>(.*?)</a>',re.DOTALL)
	a_s = p_a.findall(page_html[0])
	
	# print a_s[0][0]
	
	p_total = re.compile(r'([0-9])',re.DOTALL)
	totals = p_total.findall(a_s[0])
	total = ''
	for i in totals:
		# print i
		total = total + str(i)
	# print total
	page_num = int(total)
	return page_num
	
	# print a_s[0]
	
# start gather
def start():
	pre = 'http://www.meinv369.com'
	
	tip = 'How many album do you want to gather this time?\n'
	n = int(raw_input(tip))
	albums = db.selectAlbum(n)
	# print albums
	for album in albums:
		# print album
		album_id = album[0]
		album_url = album[7]
		print 'start to gather album ' + str(album_id)
		# print album_url
		
		# continue
		getPhotos(album_url,pre,album_id)
		db.changeAlbumIf(1,album_id)
	
host = 'localhost'
root = 'root'
pwd = ''
db = 'meinv'
chset = 'utf8'
db = MyDB(host,root,pwd,db,chset)

# saveTopics()

# saveAlbums()
# 采集只有一页的图集列表
# pre = 'http://www.meinv369.com'
# album_url = 'http://www.meinv369.com/siwa/'
# topic_id = 5
# getOnePageAlbum(album_url,topic_id,pre)

# url = 'http://www.meinv369.com/mm/mm767.html'
# getPhoto(url)
# html = getPics_module.getHtmlProxies(url)
# # print html
# # exit()
# getAlbumPage(html)

# getPhotos(url,pre,album_id)
start()
