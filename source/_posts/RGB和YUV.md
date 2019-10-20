---
title: RGB和YUV
tags:
  - opencv
  - YUV
categories: cpp

date: 2019-10-20 16:24:49
---

- 里的转图是针对RGB图片的，YUV图片没办法直接用。
- 解决办法是分开Y、U、V三个分量，分别进行转图。

```cpp
#include <iostream>
#include <opencv2/opencv.hpp>
#include <cmath>

using namespace std;
using namespace cv;

int main() {

    // 原始bgr图像
    Mat srcImage = imread("/Users/zhaijy/Desktop/test2.png");

    // 转到YVU（YV21）
    Mat dstImage;
    cvtColor(srcImage, dstImage, COLOR_BGR2YUV_YV12);

    // 前 height * width 是Y分量
    int height = srcImage.rows, width = srcImage.cols;
    Mat dstImageY = Mat(height, width, CV_8UC1);
    memcpy(dstImageY.data, dstImage.data, height * width);
    imwrite("/Users/zhaijy/Desktop/Y.jpg", dstImageY);

    // 后面 height * witdth / 4 是V分量
    Mat dstImageV = Mat(height / 2, width / 2, CV_8UC1);
    memcpy(dstImageV.data, dstImage.data + height * width, height * width / 4);
    imwrite("/Users/zhaijy/Desktop/V.jpg", dstImageV);

    // 后面 height * witdth / 4 是U分量
    Mat dstImageU = Mat(height / 2, width / 2, CV_8UC1);
    memcpy(dstImageU.data, dstImage.data + height * width * 5 / 4, height * width / 4);
    imwrite("/Users/zhaijy/Desktop/U.jpg", dstImageU);

    // Y旋转
    int rot_height = static_cast<int>(floor(sqrt(height * height + width * width) / 4)) * 4;
    Point2f center(static_cast<float>(width / 2.), static_cast<float>(height / 2.));
    Mat rot_mat = getRotationMatrix2D(center, 45, 1.0);
    Mat rotImageY = Mat(rot_height, rot_height, CV_8UC1);
    warpAffine(dstImageY, rotImageY, rot_mat, Size(rot_height, rot_height), INTER_LINEAR);
    imwrite("/Users/zhaijy/Desktop/rotY.jpg", rotImageY);

    // U旋转
    int rot_height_uv = rot_height / 2;
    Point2f center_uv(static_cast<float>(width / 4.), static_cast<float>(height / 4.));
    Mat rot_mat_uv = getRotationMatrix2D(center_uv, 45, 1.0);
    Mat rotImageU = Mat(rot_height / 2, rot_height / 2, CV_8UC1);
    warpAffine(dstImageU, rotImageU, rot_mat_uv, Size(rot_height_uv, rot_height_uv), INTER_LINEAR);
    imwrite("/Users/zhaijy/Desktop/rotU.jpg", rotImageU);

    // V旋转
    Mat rotImageV = Mat(rot_height / 2, rot_height / 2, CV_8UC1);
    warpAffine(dstImageV, rotImageV, rot_mat_uv, Size(rot_height_uv, rot_height_uv), INTER_LINEAR);
    imwrite("/Users/zhaijy/Desktop/rotV.jpg", rotImageV);

    // 拼接YVU
    Mat rotImageYVU = Mat(rot_height * 3 / 2, rot_height, CV_8UC1);
    memcpy(rotImageYVU.data, rotImageY.data, rot_height * rot_height);
    memcpy(rotImageYVU.data + rot_height * rot_height, rotImageV.data, rot_height * rot_height / 4);
    memcpy(rotImageYVU.data + rot_height * rot_height * 5 / 4, rotImageU.data, rot_height * rot_height / 4);

    // 转回BGR
    Mat rotImageBGR;
    cvtColor(rotImageYVU, rotImageBGR, COLOR_YUV2BGR_YV12);
    imwrite("/Users/zhaijy/Desktop/rotImageBGR.jpg", rotImageBGR);

    return 0;
}
```

- 然后贴一些中间的图片

![test2](/images/test2.png)

<center>原始图片</center>

![Y](/images/Y.jpg)

![V](/images/V.jpg)

![U](/images/U.jpg)

<center>分别是YVU分量</center>

![rotY](/images/rotY.jpg)

![rotV](/images/rotV.jpg)

![rotU](/images/rotU.jpg)

<center>分别是旋转后的YVU分量</center>

![rotImageBGR](/images/rotImageBGR.jpg)

<center>最后拼接完的效果</center>

- 我看YVU的解释说，$U=B-Y$，$V=R-Y$，可能是因为这个，黑边变成了绿边了吧