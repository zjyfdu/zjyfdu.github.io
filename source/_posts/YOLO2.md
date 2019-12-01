---

title: YOLO2
tags: yolo
typora-root-url: ../../source
date: 2019-10-20 21:26:31
---

9102年都快结束了，我才开始真正看yolov2

#先复习一下[yolov1](https://zhuanlan.zhihu.com/p/32525231)

- 输出的shape是$7\times7\times30$，分别是类别，置信度和坐标，虽然每个格子输出两个框，但只有一组类别
- 坐标$x, y$是相对于每一个格的，$w, h$是相对于整个图的，这样做的好处是位置坐标的取值范围都是$[0, 1]$

![preview](/images/v2-8630f8d3dbe3634f124eaf82f222ca94_r.jpg)

- loss都统一认为是回归问题

![preview](/images/v2-45795a63cdbaac8c05d875dfb6fcfb5a_r.jpg)