import re
import urllib2
import json

# url = 'http://www.4493.com/xingganmote/'

url = 'http://www.4493.com/xingganmote/index-6.htm'

# save file
def save_file(data,filename):
	f = file(filename,'ab')
	f.write(data)
	f.close()

html = urllib2.urlopen(url).read()

pattern = re.compile(r'<div class="all_lanmu ping">.*?<div class="clearh10"></div>.*?<ul>(.*?)</ul>.*?</div>',re.DOTALL)
data1 = pattern.findall(html)

print data1[0]


	
pattern_li = re.compile(r'<li>(.*?)</li>',re.DOTALL)
data2 = pattern_li.findall(data1[0])



for i in data2:
	data3 = ''
	data3 += i + '\r\n'
	save_file(i,'li.txt')
	
pattern_href = re.compile(r'href="(.*?)"',re.DOTALL)
hrefs = pattern_href.findall(data1[0])

# print hrefs

pattern_srcs = re.compile(r'src="(.*?)"',re.DOTALL)
srcs = pattern_srcs.findall(data1[0])
# print srcs

pattern_span = re.compile(r'<span>(.*?)</span>',re.DOTALL)
spans = pattern_span.findall(data1[0])
# print spans

m = len(hrefs)

albums = []
for j in range(0,m):
	album = {
		'cover'	:	unicode(srcs[j] , errors='ignore'),
		'url'	:	unicode(hrefs[j], errors='ignore'),
		'title':	spans[j].decode('gbk','ignore')
	}
	
	# print album
	print spans[j]
	
	albums.append(album)
	
# print albums
# albums = unicode( albums , errors='ignore')
encodedjson = json.dumps(albums)
# print repr(obj)
print encodedjson
save_file(encodedjson,'json.txt')	

album = {
	'cover'	:	'cover_url',
	'url'	:	'album_url',
	'title':	'text'	
}
# print album