---
title: openCV 总结
date: 2018-07-04 12:19:14
tags: openCV
categories: cpp
---
# 一些图像操作
- [腐蚀与膨胀(Eroding and Dilating)](http://www.opencv.org.cn/opencvdoc/2.3.2/html/doc/tutorials/imgproc/erosion_dilatation/erosion_dilatation.html)，膨胀腐蚀都是针对亮色区域说的，膨胀是取最大值，腐蚀是最小值，实现的话，最直接的方法是四个for循环

- **开运算**：腐蚀+膨胀，可以去除图中的小白点；**闭运算**：膨胀+腐蚀，可以去除图片中的小黑点

- **top hat**：原图-开，得到的是开运算中被去掉的小白点；**black hat**：原图-闭，得到闭运算中去掉的小黑点

- [霍夫线变换](https://www.cnblogs.com/skyfsm/p/6902524.html)

- 直方图均衡化

```cpp
cv::equalizeHist(srcmat, dstmat);

cv::Mat lookup(1, 256, CV_8U);
// p[i] 是强度小于等于i的比例
lookup.at<uchar>(i) = static_cast<uchar>(255.0 * p[i]);
dstmat = applyLookUp(srcmat, lookup);
```

# C的接口
- 字体的说明参考[这里](https://blog.csdn.net/longzaitianya1989/article/details/8121286)
- cvReleaseImage，只是将IplImage*型的变量值赋为NULL，而这个变量本身还是存在的并且在内存中的存储位置不变
- `iplimg->imageSize == iplimg->height * iplimg->widthStep`，而不是f`rame->height * frame->width`
- `iplimg->imageData`是对齐的内存，[官方文档](https://docs.opencv.org/3.4/d6/d5b/structIplImage.html)说`iplimg->imageDataOrigin`是没有对齐的内存，还没有验证过
- 默认的存储方式是BGR，不是RGB

```c
// 读图
IplImage* iplimg = cvLoadImage("heels.jpg");

// 把cv::mat改为c的图
*iplimg = IplImage(matimg);

// 创建新图，最后一个参数是channel数
IplImage* iplimg=cvCreateImage(cvSize(360, 640), IPL_DEPTH_8U, 3);

// 显示图
cvNamedWindow("img", 0);  
cvShowImage("img", iplimg);  
cvWaitKey(0);  

// 打印字
CvFont font;
cvInitFont(&font, CV_FONT_HERSHEY_COMPLEX, 0.5, 0.5, 1, 2, 8);  
cvPutText(iplimg, "This is a picture named lena!", cvPoint(50, 50), &font, CV_RGB(255,0,0));

// 保存图
cvSaveImage("c:\\test1.jpg", iplimg);  
```

# C++的接口

```c++
// 读图
cv::Mat matimg = cv::imread ("heels.jpg");

// 把IplImage改为c++接口，第二个参数是需不需要拷贝，默认是false
matimg = cv::Mat(iplimg, false);

// 创建新图，CV_8UC3是三通道，CV_8UC1是单通道
cv::Mat matimg(2, 2, CV_8UC3, Scalar(0,255,0));

// 显示图
cv::nameWindow("img");
cv::imshow("img", matimg);
cv::waitKey(-1);  

// 打印字
// void putText(Mat& img, const string& text, Point org, int fontFace, double fontScale, Scalar color, int thickness=1, int lineType=8, bool bottomLeftOrigin=false )
cv::putText(image, "opencv", Point(5,100), FONT_HERSHEY_DUPLEX, 1, Scalar(0,143,143), 2);

// 保存图，后缀名决定了图片对编码格式
cv::imwrite("c:\\test1.jpg", matimg);

// 遍历图像
// Vec3b表示三通道usigned char类型，
// 还可以有2通道和4通道，类型还可以有f(loat)、i(nt)、d(ouble)、s(hort)、w(unsigned short)
// typedef Vec<float, 2> Vec2f;
matimg.at<cv::Vec3b>(j,i)[channel] = value;

// 还可以直接取每一行对首地址
uchar* data = matimg.ptr<uchar>(j);
```

# 头文件分析
- 一般直接包含这三个头文件

```
#include<opencv2/core/core.hpp>
#include<opencv2/imgproc/imgproc.hpp>
#include<opencv2/highgui/highgui.hpp>
```
