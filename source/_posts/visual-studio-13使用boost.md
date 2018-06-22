---
title: visual studio 13使用boost
date: 2018-06-22 11:17:03
tags:
---

### 步骤
- 先去[boost官方网站](http://www.boost.org/)中查看boost的最新版本，然后去相应的链接地址进行下载
- 在你创建好的工程项目中，选择属性对话框，然后在VC++目录选项中，把boost路径添加到包含目录和库目录中
- 首选运行bootstra.bat，如果没有cl命令的话，查看[这里](https://blog.csdn.net/zhidebushizhan/article/details/51396670)，我是这个命令`call "%VS120COMNTOOLS%"vsvars32.bat`解决问题
- `bjam address-model=64 link= static  threading=multi  variant=release  runtime-link=shared  stage`

### 困惑的地方
- vs里面的vc++目录和下面的c++目录、连接器目录，什么关系啊，能自动加载子目录？
- bjam里面的debug release、static share是啥。。。

### 参考
- https://blog.csdn.net/blues1021/article/details/45034133
- https://blog.csdn.net/qingyulove/article/details/78863457
- https://blog.csdn.net/zhidebushizhan/article/details/51396670