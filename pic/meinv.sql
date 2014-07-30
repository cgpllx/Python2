-- 美女图片数据库
CREATE DATABASE meinv DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

USE meinv;

SET NAMES utf8;

CREATE table meinv_topic
(
	topic_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	topic_title VARCHAR(250) NOT NULL COMMENT '图片分类',
	topic_url VARCHAR(250) NOT NULL COMMENT '分类URL',
	topic_if  TINYINT NOT NULL DEFAULT 0 COMMENT '该栏目下的图集地址是否已经采集完毕，0--未采集，1--已经采集'
)ENGINE=MyISAM DEFAULT CHARSET utf8;

CREATE TABLE meinv_album
(
	album_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	topic_id INT NOT NULL COMMENT '图集所属的分类ID',
	album_title VARCHAR(250) NOT NULL COMMENT '图集标题',
	album_thumb_net VARCHAR(250) NOT NULL COMMENT '图集封面网络地址',
	album_thumb VARCHAR(250) NOT NULL COMMENT '图集封面本站地址',
	album_url VARCHAR(250) NOT NULL COMMENT '图集URL',
	album_to INT NOT NULL DEFAULT 0 COMMENT '采集到了图集的第几页',
	album_if TINYINT NOT NULL DEFAULT 0 COMMENT '图集是否已经采集完毕，0--未采集，1--已经采集'
)ENGINE=MyISAM DEFAULT CHARSET utf8;

CREATE TABLE meinv_picture
(
	picture_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	album_id INT NOT NULL COMMENT '图片所属的图集ID',
	picture_net VARCHAR(250) NOT NULL COMMENT '图片网络地址',
	picture_url VARCHAR(250)  COMMENT '图片本站地址',
	picture_if TINYINT NOT NULL DEFAULT 0 COMMENT '图片是否已经采集，0--未采集，1--已经采集'
)ENGINE=MyISAM DEFAULT CHARSET utf8;