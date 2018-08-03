---
title: python 里的字符串编码问题
tags:
  - 编码
  - 字符串
categories: python 
date: 2018-08-03 14:29:40
---

https://blog.csdn.net/ktb2007/article/details/3876436
打印unicode是不会乱码的

python3 里的字符串默认是unicode，python2里默认是bytes
u"python2" = "python3"
b"python3" = "python2"

不是仅仅是针对中文, 可以针对任何的字符串，代表是对字符串进行unicode编码

