---
title: mobileNet和shuffleNet
date: 2018-05-13 13:05:50
categories: caffe
---

### 先说mobileNet
- 使用depthwise convolution和point wise(1*1) convolution代替标准的convolution
![](/images/8709950.jpg)
- (b)类似于group为M的卷积，m-th filter is applied to m-th channel
- 计算量是原来的$\frac{1}{N}+\frac{1}{D_k^2}$，kernel一般是3，所以可以减少到1/8到1/9
- 论文里还提出了两个控制计算量的超参数
- width multiplier，$\alpha$，乘在channel前面，计算量减小到$\frac{1}{\alpha}$
- resolution multiplier，$\beta$，乘在输入到尺寸前面，计算量减小到$\frac{1}{\beta}$
- 好像文章里公式写错了，卷积到计算量应该是乘输出的尺寸，而不是输入到尺寸吧。。。

### [shuffleNet](https://blog.csdn.net/u014380165/article/details/75137111)
- 在resnet的基础上，用带group的1\*1卷积代替原来的1\*1卷积
![](/images/32435128.jpg)
- group操作会带来边界效应，学出来的特征会局限，所以就有了channel shuffle层
- 随机层的caffe实现是先reshape再transpose再flatten，不是真随机，所以可以实现backward
- 3\*3的depth wise的卷积就是moblieNet里用到的
- 然后用shuffleNet Unit组成shuffetNet网络
![](/images/77705439.jpg)
- 一个重要结论是group个数的线性增长并不会带来分类准确率的线性增长。但是发现ShuffleNet对于小的网络效果更明显，因为一般小的网络的channel个数都不多，在限定计算资源的前提下，ShuffleNet可以使用更多的feature map。

