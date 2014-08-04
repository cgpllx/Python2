# coding=utf-8
# 线程
import time
import thread
import urllib2

def get_html(url):
	html = urllib2.urlopen(url).read()
	return html

# 保存网页
def save_html(data,filename):
	f = file(filename,'wb')
	f.write(data)
	f.close()
	
def test(url,i):	
	print 'gather %s: \n' % (url)
	t = str(time.time())	
	s = t.split('.')
	filename = s[0] + s[1] + '-' + str(i) + '.html'	
	data = get_html(url)	
	save_html(data,filename)
	thread.exit()


# 为线程定义一个函数
def print_time(threadName,delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count +=1
		print "%s:%s\n" % (threadName,time.ctime(time.time()))


url1 = 'http://www.ifeng.com'
url2 = 'http://www.qq.com'
url3 = 'http://re.ihopes.cn'
url4 = 'http://www.wangye.com'
url5 = 'http://www.4399.com/'
url6 = 'http://www.hexun.com/'

		
# 创建两个线程
try:
	thread.start_new_thread(test,(url1,1,))
	thread.start_new_thread(test,(url2,2,))
	thread.start_new_thread(test,(url3,3,))
	thread.start_new_thread(test,(url4,4,))
	thread.start_new_thread(test,(url5,5,))
	thread.start_new_thread(test,(url6,6,))
except SystemExit:  
    # pass
	print 'over'
	# exit()
except:  
    traceback.print_exc()

	
while 1:
	# print 'over2'
	# exit()
	pass
	
