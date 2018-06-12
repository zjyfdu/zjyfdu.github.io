---
title: 吴恩达deeplearning.ai课程学习笔记
date: 2018-01-16 16:32:21
tags: 学习笔记
categories: caffe
---

### 0. 前言

[作业在这里](https://github.com/zjyfdu/deeplearning.ai)
原仓库被coursera要求删掉了，多亏我及时folk/斜眼笑

[视频可以直接在网易上看](https://mooc.study.163.com/smartSpec/detail/1001319001.htm)

### 1. 神经网络前馈和后馈

![](http://ot0uaqt93.bkt.clouddn.com/18-1-23/89948814.jpg "前馈")
![](http://ot0uaqt93.bkt.clouddn.com/18-1-23/41005456.jpg "后馈")
如果没有激活函数的话，多层的神经网络仍然是个线性的模型。
![](http://ot0uaqt93.bkt.clouddn.com/18-1-23/73637538.jpg "激活函数")

### 2. 超参数、正则化、优化算法等

L2正则化相当于是w权重减小， weight decay
![](http://ot0uaqt93.bkt.clouddn.com/18-1-23/69146591.jpg)
后面等这些是用在mini-batch中的，当训练数据量太大，需要对训练数据分割为mini-batch。但这样会造成收敛方向波动，为了减小这种波动，引入Adam优化算法。
![](http://ot0uaqt93.bkt.clouddn.com/18-1-23/27110293.jpg "指数加权平均")
![](http://ot0uaqt93.bkt.clouddn.com/18-1-23/27110293.jpg)
![](http://ot0uaqt93.bkt.clouddn.com/18-1-23/47657351.jpg)
![](http://ot0uaqt93.bkt.clouddn.com/18-1-23/306118.jpg)
batch norm
![](http://ot0uaqt93.bkt.clouddn.com/18-1-23/49641113.jpg)
![](http://ot0uaqt93.bkt.clouddn.com/18-1-23/54964765.jpg)

### 3. CNN

~~待续~~

[感觉这篇已经总结得很好了](https://mp.weixin.qq.com/s/kvbDQ2d7iZ2cur2CQ_e-1Q)