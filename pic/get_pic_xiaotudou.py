# coding=utf-8
# get picture from http://tu.xiaotudou.net/meinv/
# Filename:get_pic_xiaotudou.py


import getPics_module
import re

url = 'http://tu.xiaotudou.net/meinv/'
html = getPics_module.getHtml(url)

getPics_module.saveHtml(html,'3692.txt')

# print html
pattern_topic = '<div class="nav">(.*?)</div>'
topics = getPics_module.getTopic(pattern_topic,html)
# print topics

