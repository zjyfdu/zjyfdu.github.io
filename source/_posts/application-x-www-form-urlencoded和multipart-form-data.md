---
title: application/x-www-form-urlencoded和multipart/form-data
date: 2018-01-30 14:17:47
categories: flask网站总结
---

[抄自这里](http://www.cnblogs.com/taoys/archive/2010/12/30/1922186.html)

> form的enctype属性为编码方式，常用有两种：`application/x-www-form-urlencoded`和`multipart/form-data`。

> 默认为`application/x-www-form-urlencoded`。 当action为get时候，浏览器用x-www-form-urlencoded的编码方式把form数据转换成一个字串（name1=value1&name2=value2...），然后把这个字串append到url后面，用?分割，加载这个新的url。 当action为post时候，浏览器把form数据封装到http body中，然后发送到server。 

> 如果没有type=file的控件，用默认的`application/x-www-form-urlencoded`就可以了。 但是如果有type=file的话，就要用到`multipart/form-data`了。浏览器会把整个表单以控件为单位分割，并为每个部分加上Content-Disposition(form-data或者file),Content-Type(默认为text/plain),name(控件name)等信息，并加上分割符(boundary)。

[更详细的](http://blog.csdn.net/xiaojianpitt/article/details/6856536)
