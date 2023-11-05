---
title: Attention
typora-root-url: ../../source
tags: Attention
categories: caffe
date: 2019-03-04 22:31:36
---

# Content Attention
- 假设cnn之后，feature map是$T\times1$，用$x$表示，这里用caffe的表示方法，宽度在前，高度在后，忽略了batch size
- Content Attention是最常见的Attention，计算权重只用到了$x$和LSTM的输出$c_{t-1}$，$c_{t-1}$和$x$都需要一个全连接
- 其实这里的$\hat{e}_{t,j},  j=1..T$是一起算的，$wx$的shape已经是$T\times C$，而$wc_{t-1}$是$1\times C$，需要扩增到$T\times C$
$$
\hat{e}_{t,j}=wc_{t-1}+wx_j \\
e_{t,j}=tanh(\hat{e}_{t,j}) \\
\alpha_{t,j}=softmax(we_{t,j})
$$
- $\alpha_t$的shape是$T\times1$，是$x$每个位置的权重，然后进行累加，$g_t$称之为glimpse向量，
$$
g_t=\sum_{j=1}^{T}\alpha_{t,j}x_j
$$
- 然后用LSTM解码，这里$y_{t-1}+g_t$其实是不能直接加到，shape不一致，需要先对$y_{t-1}$全连接一下
$$
c_t,h_t=LSTM(y_{t-1}+g_t, c_{t-1}) \\
y_t=argmax(softmax(wh_t))
$$

# Hybrid Attention
- Content有一个严重对问题是计算权重对时候，只用到了内容信息，没有用到位置信息，所以会出现对不齐对问题
- Hybrid Attention其实是Content Attention和Locate Attention的混合，区别只是体现在$\hat{e}_{t,j}$的计算上多了上一时刻的位置信息
$$
\hat{e}_{t,j}=wc_{t-1}+wx_j+w\alpha_{t-1,j}
$$
- $\alpha_{t-1,j}$的shape是$T\times N\times1$，先换成$N\times T\times1$，然后用$1\times1$的卷积，卷成$N\times T\times C$，然后可以全连接，最后再换回$T\times N\times C$，这样就能加起来了
