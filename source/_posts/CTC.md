---
title: CTC
date: 2018-03-20 14:48:40
tags:
  - CTC
categories: caffe
---

- 以OCR为例，原始图片经过CNN卷积，图片高度方向尺寸变为1
- 图片的宽度方向即为时间序列方向
- 在channel分享进行innerproduct，然后softmax，得到每个序列在每个字符的概率，类似于下面这张图
![](https://img-blog.csdn.net/20170809180923623)

- 然后根据这个概率图，使用类似动态规划的思路，可以计算出ctc loss和导数

- 不想写了，看下面这篇吧

- [CTC讲解](http://blog.csdn.net/luodongri/article/details/77005948)
