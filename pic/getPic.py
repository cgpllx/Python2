#Filname: getPic.py

import urllib2
import re

def saveFile(path,data):
	f = file(path,"wb")
	f.write(data)
	f.close()

url = 'http://www.mnsfz.com/h/yangguang/PiaCabJHeaiaiPbiH.html'
pic = re.compile(r'img src="([^>]*?jpg)"',re.DOTALL)
html = urllib2.urlopen(url).read()
pics = pic.findall(html)
# print pics
path = 'E:/pics/'
i = 0
for p in pics:
	# print p
	data = urllib2.urlopen(p).read()
	path2 = str(i) + str(i) + '.jpg'	
	print path2
	saveFile(path2,data)
	i = i + 1
	
	
	
