---
title: python 里的字符串编码问题
tags:
  - 编码
  - 字符串
  - unicode
categories: python 
date: 2018-08-03 14:29:40
---

### 丑陋的编码

python中有很多地方涉及到编码，简直丑陋

- 文本编辑器可以选编码格式，一般都位于右下角
- python文件开头有`#coding: utf-8`
- python还有默认encoding
```python
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
```
- 字符串前有u和b

### [一些编码知识](https://blog.ernest.me/post/python-setdefaultencoding-unicode-bytes)

- unicode是个大集合，支持百万级别的字符，但unicode只是给每个字符进行了一个编码，没有给具体实现
- utf-8是unicode的一种实现形式，除此之外还有utf-16等等
- gb系列的编码和unicode没啥关系，GB2312 < GBK < GB18030
- windows中文版系统的默认编码是gbk的

### 一些python的知识

- python里有三种string类，unicode（text string）、str（byte string）、basestring。basestring是前两个的父类
- python里，字节串就等同于字符串
- 在类型转换或和文本拼接时，需要确定字节串的编码，不然就不能转换。python2的年代，默认的encoding是ASCII，放现在当然是不够用的
- python3终于把默认的编码变成unicode
- str转换成unicode，在python里叫decode，unicode转换成str称之为encode
- 打印unicode是不会出错的，这就是python3的厉害，打印str的话，就要看打印编码式和你显示的编码是否一致了

### 这些编码的区别

- 文本编码格式：只和你的编辑器有关，负责把你的python文件按这种格式保存
- python文件开头的coding：告诉python解释器，文件是按什么格式保存的，所以要与你实际文件的保存格式一致。如果不写的话，python文件里只能有ASCII。
- 默认的encoding格式就是你要告诉系统，字节码以哪种格式转换成unicode
- u是指后面引号里的内容是unocide，b是指引号里面的内容是str，所以python3里写u是没用的，python2里写b是没用的

### 最佳实践

- 换python3
- [如果换不了python3](https://blog.ernest.me/post/python-setdefaultencoding-unicode-bytes)
  - 所有 text string 都应该是 unicode 类型，而不是 str
  - 在需要转换的时候，显式转换。从字节解码成文本，用 var.decode(encoding)，从文本编码成字节，用 var.encode(encoding)
  - 从外部读取数据时，默认它是字节，然后 decode 成需要的文本；同样的，当需要向外部发送文本时，encode 成字节再发送。



