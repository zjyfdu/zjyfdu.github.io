---
title: mobileNet和shuffleNet
date: 2018-05-13 13:05:50
tags:
---

### 先说mobileNet
- [链接]()
- 使用depthwise convolution和1*1 convolution代替标准的convolution
- 这里放个图片和公式
- depthwise的caffe实现在[这里]()

### shuffleNet
- 使用group convolution代替mobileNet中的1*1 convolution
- 引入channel随机层
- 随机层的caffe实现在[这里]()，思路是先reshape再transpose再flatten，所以可以实现backword
- 这里放shuffleNet Unit的图
