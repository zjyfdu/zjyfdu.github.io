---
title: python 里的字符串编码问题
tags:
  - 编码
  - 字符串
  - unicode
categories: python 
date: 2018-08-03 14:29:40
---

### 大背景

python中有很多地方涉及到编码，简直丑陋

- 文本编辑器可以选编码格式，一般都位于右下角
- python文件开头有`#coding: utf-8`
- python还有默认encoding
```
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
```
- 字符串前有u和b

### 一些编码知识

- unicode是个大集合，支持百万级别的字符，但unicode只是给每个字符进行了一个编码，没有给具体实现
- utf-8是unicode的一种实现形式，除此之外还有utf-16等等
- gb系列的编码和unicode没啥关系，GB2312 < GBK < GB18030

### 一些python的知识

- python里有三种string类，unicode（text string）、str（byte string）、basestring。basestring是前两个的父类。
- python里，字节串就等同于字符串。
- 在类型转换或和文本拼接时，需要确定字节串的编码，不然就不能转换。python2的年代，默认的encoding是ASCII，当然放现在是不够用的。


https://blog.csdn.net/ktb2007/article/details/3876436
打印unicode是不会乱码的

python3 里的字符串默认是unicode，python2里默认是bytes
u"python2" = "python3"
b"python3" = "python2"

不是仅仅是针对中文, 可以针对任何的字符串，代表是对字符串进行unicode编码

### 参考资料
https://blog.ernest.me/post/python-setdefaultencoding-unicode-bytes
http://www.ruanyifeng.com/blog/2007/10/ascii_unicode_and_utf-8.html


