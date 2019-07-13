---
title: visual studio 13使用boost
typora-root-url: ../../source
date: 2018-06-22 11:17:03
categories: cpp
---

### 步骤
- 先去[boost官方网站](http://www.boost.org/)中查看boost的最新版本，然后去相应的链接地址进行下载
- 在你创建好的工程项目中，选择属性对话框，然后在VC++目录选项中，把boost路径添加到包含目录和库目录中
- 首选运行bootstra.bat，如果没有cl命令的话，查看[这里](https://blog.csdn.net/zhidebushizhan/article/details/51396670)，我是这个命令`call "%VS120COMNTOOLS%"vsvars32.bat`解决问题
- 生成动态链接的静态库`bjam address-model=64 link= static  threading=multi  variant=release  runtime-link=shared  stage`

### 困惑的地方
- vs里面的vc++目录和下面的c++目录、连接器目录，什么关系啊，能自动加载子目录？


> 引用自[这里](https://www.cnblogs.com/JMLiu/p/7954630.html)，
> VC++ Directories是一个Windows环境变量，C/C++是命令行参数，这是本质区别；
> 但是相同的项，也就是VC++ Directories中的include directories 对应到C/C++中的addition include directories 是一样的效果，也就是说效果一样。同样是命令行参数的还有Link设置，Link设置中的 addition library directories对应到VC++ Directories 中的library directories，也就是说，效果是相同的。

- bjam里面的debug release、static share是啥。。。

> 编译调试版本加 debug

> 编译发布版本加  release

> 编译静态链接库：link=static runtime-link=static

> 编译动态库：link=shared runtime-link=shared

> 静态库只是需要的文件编译到exe/so中，而且shared的是否用户也要存在dll,所以static是更安全的方式；当然组件式开发和升级的软件用shared方式更加合适

### 参考
- https://blog.csdn.net/blues1021/article/details/45034133
- https://blog.csdn.net/qingyulove/article/details/78863457
- https://blog.csdn.net/zhidebushizhan/article/details/51396670
