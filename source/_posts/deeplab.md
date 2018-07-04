---
title: deeplab
date: 2018-06-19 21:13:20
categories: caffe
---
今天看了deeplab-V1的论文，不是很清楚，先大概记一下

### 背景
- 问题背景是语义分割，semantic segmentation。
- FCN通过转置卷积和上采样，把feature map还原到原图尺寸

### v1
- feature map的感受野的计算公式为$RF_{i+1}=(RF_i-1)*stride+kernel$
- hole算法，在kernel里面增加“hole”，kernel size变大
- 在VGG16最后两层去掉pooling，使用hole卷积
- CRF简单来说，能做到的就是在决定一个位置的像素值时（在这个paper里是label），会考虑周围邻居的像素值（label），这样能抹除一些噪音。但是通过CNN得到的feature map在一定程度上已经足够平滑了，所以short range的CRF没什么意义。于是作者采用了fully connected CRF，这样考虑的就是全局的信息了。
- CRF，条件随机场，具体可以看[这里](https://www.jianshu.com/p/434b3e22a47e)

### v2
- [这里](https://blog.csdn.net/ming0808sun/article/details/78843471)
- [这里](https://blog.csdn.net/u012759136/article/details/52434826#t9)

