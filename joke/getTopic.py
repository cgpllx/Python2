# encoding:utf8
# Filename: getTopic.py

import re
import urllib2

class Joke:
	# get topic start
	def getHtml(self,url):
		try:
			html = urllib2.urlopen(url).read()
			return html
		except:
			pass
	
	# get topic table
	def getTopicTable(self,html):
		try:
			pattern = re.compile(r'<table.*?id="classlist"[^>]*?>(.*?)</table>',re.DOTALL)
			topicTable = pattern.findall(html)
			return topicTable[0]
		except:
			pass
	
	# get url and name of a topic
	def getTopicUrlName(self,html):
		try:
			pattern_topic = re.compile(r'<a.*?href="(.*?)"[^>]*?>(.*?)\(\d{0,}\)</a>',re.DOTALL)
			match_topic = pattern_topic.findall(html)
			# print match_topic
			return match_topic
		except:
			pass
	
	# test
	def test(self,url):
		html = self.getHtml(url)
		# print html
		topicTable = self.getTopicTable(html)
		# print topicTable
		topic_url_name = self.getTopicUrlName(topicTable)
		return topic_url_name

# test
joke = Joke()
url = 'http://www.jokeji.cn/Keyword.htm'
topic_info = joke.test(url)
print topic_info
for t in topic_info:
	print t[0]
	print t[1]
else:
	print 'over'


