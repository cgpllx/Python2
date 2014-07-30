# Filename: getDouban_save.py

import MySQLdb

class MyDB:
	# Initialize a conn
	def __init__(self,host,root,pwd,db,chset):
		try:
			self.conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '', db = 'meinv', charset = 'utf8')
			self.cur = self.conn.cursor()
		except MySQLdb.Error,e:
			print 'Mysql Error %d: %s' % (e.args[0], e.args[1])
			
	# save log
	def saveError(self,msg,filename):
		f = file(filename,'a+')
		f.write(msg)
		f.close()
		
	# save chapter 
	def saveTopic(self,topic_title,topic_url):
		try:
			value = [topic_title,topic_url]
			# sql = 'INSERT INTO mo_tag (kind_id, tag_name, tag_url) VALUES (%s, %s, %s)'
			sql = 'INSERT INTO meinv_topic (topic_title,topic_url) VALUES (%s, %s)'
			self.cur.execute(sql,value)
			self.conn.commit()
		except MySQLdb.Error,e:
			print 'MySQL Error %d: %s' %s (e.args[0], e.args[1])
	

	# save album
	def saveAlbum(self,topic_id,album_title,album_thumb_net,album_url):
		try:
			value = [topic_id,album_title,album_thumb_net,album_url]
			# sql = 'INSERT INTO mo_tag (kind_id, tag_name, tag_url) VALUES (%s, %s, %s)'
			sql = 'INSERT INTO meinv_album (topic_id,album_title,album_thumb_net,album_url) VALUES (%s, %s, %s, %s)'
			self.cur.execute(sql,value)
			self.conn.commit()
			return True
		except MySQLdb.Error,e:
			print 'MySQL Error %d: %s' %s (e.args[0], e.args[1])
			return False
	
	
	def selectTopic(self,n):
		# sql = 'SELECT * FROM tmp_films WHERE film_if = 0 AND error_if = 0 AND film_id > 120000'
		sql = 'SELECT * FROM meinv_topic WHERE topic_if = 0'
		self.cur.execute(sql)
		res = self.cur.fetchmany(n)
		return res
		
		
	def selectAlbum(self,n):
		sql = 'SELECT * FROM meinv_album WHERE album_to = 0 AND album_if = 0'
		self.cur.execute(sql)
		res = self.cur.fetchmany(n)
		return res
		
	def selectAlbum2(self,n):
		sql = 'SELECT * FROM meinv_album WHERE album_to = 0 AND album_if = 0 ORDER BY album_id DESC'
		self.cur.execute(sql)
		res = self.cur.fetchmany(n)
		return res
		
	def saveAlbumPage(self,page,album_id):
		value = [page,album_id]
		sql = 'UPDATE meinv_album SET album_to=%s WHERE album_id=%s'
		self.cur.execute(sql,value)
		self.conn.commit()
		
	def changeAlbumIf(self,album_if,album_id):
		value = [album_if,album_id]
		sql = 'UPDATE meinv_album SET album_if=%s WHERE album_id=%s'
		self.cur.execute(sql,value)
		self.conn.commit()
		
	# save picture
	def savePicture(self,album_id,picture_net):
		try:
			value = [album_id,picture_net]
			# sql = 'INSERT INTO mo_tag (kind_id, tag_name, tag_url) VALUES (%s, %s, %s)'
			sql = 'INSERT INTO meinv_picture (album_id,picture_net) VALUES (%s, %s)'
			self.cur.execute(sql,value)
			self.conn.commit()
			return True
		except MySQLdb.Error,e:
			print 'MySQL Error %d: %s' %s (e.args[0], e.args[1])
			return False
	
	# update novel_chapter set chapter_if = 1
	def setChapterIf(self,i,j):
		value = [i,j]
		sql = 'UPDATE novel_chapter SET chapter_if=%s WHERE chapter_id=%s'
		self.cur.execute(sql,value)
		self.conn.commit()
	
	
	
	# save tag and tag url
	def saveTagUrl(self, kind_id, tag_name, tag_url):
		try:
			value = [kind_id, tag_name, tag_url]
			# sql = 'INSERT INTO mo_tag (kind_id, tag_name, tag_url) VALUES (%s, %s, %s)'
			sql = 'INSERT INTO tmp_tags (kind_id, tag_name, tag_url) VALUES (%s, %s, %s)'
			self.cur.execute(sql,value)
			self.conn.commit()
		except MySQLdb.Error,e:
			print 'MySQL Error %d: %s' %s (e.args[0], e.args[1])
	
	# save tmp files
	def saveTmpFilms(self,	film_name,	tag_id,	film_url):
		try:
			value = [film_name,	tag_id,	film_url]
			sql	=	'INSERT INTO tmp_films (film_name,	tag_id,	film_url)	VALUES	(%s,	%s,	%s)'
			self.cur.execute(sql,value)
			self.conn.commit()			
			# self.setTmpIf(1,tag_id)
			print 'save ' + film_url + ' success'
		except MySQLdb.Error,e:
			# print 'MySQL Error %d:	%s'	%s	(e.args[0],	e.args[1])
			msg = msg + '\n'
			filename = 'tmp_film_' + str(tag_id) + '.txt'
			self.saveError(msg,filename)
	# save tmp film content
	def saveTmpFilmContent(self, tag_id, tmp_title, tmp_info,  tmp_related_info):
		try:
			# value = [tag_id, MySQLdb.escape_string(tmp_title), MySQLdb.escape_string(tmp_info), MySQLdb.escape_string(tmp_related_info)]
			value = [tag_id, tmp_title, tmp_info, tmp_related_info]
			sql = 'INSERT INTO tmp_film_content (tag_id, tmp_title, tmp_info, tmp_related_info) VALUES (%s, %s, %s, %s)'
			self.cur.execute(sql, value)
			self.conn.commit()
			# print 'save success\n'
			# print tmp_title + ' save success'
		except MySQLdb.Error,e:
			# print 'MySQ Error %d: %s' %s (e.args[0], e.args[1])
			msg = 'MySQ Error %d: %s' %s (e.args[0], e.args[1]) + '\n'
			filename = 'tmp_film_content_' + str(tag_id) + '.txt'
			self.saveError(msg,filename)
		
	
	
	# select tag from tmp_tags
	def selectTags(self,n):
		sql = 'SELECT * FROM tmp_tags WHERE tag_if = 0'
		self.cur.execute(sql)
		res = self.cur.fetchmany(n)
		return res
		
	# select tmp_film from tmp_films whoes film_id > 120000
	def selectTmpFilm(self,n):
		# sql = 'SELECT * FROM tmp_films WHERE film_if = 0 AND error_if = 0 AND film_id > 120000'
		sql = 'SELECT * FROM tmp_films WHERE film_if = 0 AND error_if = 0'
		self.cur.execute(sql)
		res = self.cur.fetchmany(n)
		return res
	
	
		
	# update tmp_films set film_if=1
	def setTmpFilmIf(self,i,j):
		value = [i,j]
		sql = 'UPDATE tmp_films SET film_if=%s WHERE film_id=%s'
		self.cur.execute(sql,value)
		self.conn.commit()
		
	# update tmp_films set error_if = 1
	def setTempFilmError(self,film_id,error_if):
		value = [error_if,film_id]
		# print value
		sql = 'UPDATE tmp_films SET error_if=%s WHERE film_id=%s'
		# print sql
		# return False
		self.cur.execute(sql,value)
		self.conn.commit()
		
		
	
		
		
			
			
	