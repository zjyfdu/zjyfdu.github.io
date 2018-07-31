---
title: openCV 总结
date: 2018-07-04 12:19:14
tags: openCV
categories: cpp
---

- [腐蚀与膨胀(Eroding and Dilating)](http://www.opencv.org.cn/opencvdoc/2.3.2/html/doc/tutorials/imgproc/erosion_dilatation/erosion_dilatation.html)
> 此操作将图像 A 与任意形状的内核 (B)，通常为正方形或圆形,进行卷积。内核 B 有一个可定义的 锚点, 通常定义为内核中心点。进行膨胀操作时，将内核 B 划过图像,将内核 B 覆盖区域的最大相素值提取，并代替锚点位置的相素。显然，这一最大化操作将会导致图像中的亮区开始”扩展” (因此有了术语膨胀 dilation )。

- [霍夫线变换](https://www.cnblogs.com/skyfsm/p/6902524.html)

- IplImage是OpenCV中C语言的图像类型;cv::Mat是OpenCV中C++语言的图像类型。[这里](https://blog.csdn.net/caroline_wendy/article/details/16940895)
- cvReleaseImage，只是将IplImage*型的变量值赋为NULL，而这个变量本身还是存在的并且在内存中的存储位置不变
- [c和c++的opencv区别](https://blog.csdn.net/jdk_yxs/article/details/64921975)