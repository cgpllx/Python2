-- 网络小说数据库
CREATE DATABASE novel DEFAULT CHARACTER SET UTF8 COLLATE utf8_general_ci;

USE novel;

-- SET NAMES utf8;

CREATE TABLE novel_book_name
(
	book_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	type_id INT NOT NULL COMMENT '小说类别',
	name VARCHAR(250) NOT NULL COMMENT '书名'
)ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE novel_chapter
(
	chapter_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	book_id INT NOT NULL COMMENT '本章所属书籍ID',
	chapter_title VARCHAR(250) NOT NULL COMMENT '本章标题',
	chapter_url VARCHAR(250) NOT NULL COMMENT '本章的URL',
	chapter_if TINYINT NOT NULL DEFAULT 0 COMMENT '是否采集，0--未采，1--已采'
)ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE novel_content
(
	content_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	chapter_id INT NOT NULL COMMENT '该内容的章节标题ID',
	content_text TEXT NOT NULL COMMENT '小说内容',
	content_if TINYINT NOT NULL DEFAULT 0 COMMENT '是否采集，0--未采，1--已采'	
)ENGINE=MyISAM DEFAULT CHARSET=utf8;

INSERT INTO novel_book_name (type_id,name)
VALUES (1,'恋上嫂子的床');