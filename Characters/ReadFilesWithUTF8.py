#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 11:11
# @Author  : Colin
# @Site    : https://github.com/DreamsFuture
# @File    : ReadFilesWithUTF8.py
# @Software: PyCharm Community Edition

# 编码U表示为Unicode编码
str = u'中国人在这里！'

#  把Unicode编码的字符使用utf-8编码
str_utf8 = str.encode('utf-8')

#  输出时用utf-8解码
for each_unicode_character in str_utf8.decode('utf-8'):
    print(each_unicode_character)

open('file.txt').read().decode('utf-8').split()



#在一个文件中打开编解码内容
import io

with io.open('result.txt', encoding='utf-8') as file:
    words = [word for line in file for word in line.split()]
print( "\n".join(words))