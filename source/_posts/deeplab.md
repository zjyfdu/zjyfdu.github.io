---
title: deeplab
date: 2018-06-19 21:13:20
categories: caffe
---

# v1

## Atrous algorithm

- deeplab和FCN一样，也是在VGG上finetune
- 首先要解决的问题是，如何增大最后输出的score map呢？deeplab把VGG最后的pool4和pool5的stride从2变成了1，整个VGG的stride从32变成8
- 但是修改了stide之后，后面的conv层感受野就不一样大了，不能finetune了，所以这里引入了非常优雅的atrous algorithm
  - feature map的感受野的计算公式为$RF_{i}=(RF_{i+1}-1)*stride+kernel$
  - 所以在stride减小的情况下想办法增大kernel，即在kernel里面增加hole，kernel变大

![deeplab](/images/70081567.jpg)

## Fully connected CRF

- CRF简单来说，能做到的就是在决定一个位置的像素值时（在这个paper里是label），会考虑周围邻居的像素值（label），这样能抹除一些噪音。但是通过CNN得到的feature map在一定程度上已经足够平滑了，所以short range的CRF没什么意义。于是作者采用了fully connected CRF，这样考虑的就是全局的信息了。
- 随机变量$X_i$是像素$i$的标签，变量$X$由$X_1, X_2, ..., X_N$组成随机向量，$N$就是图像中的像素个数。
- 在全连接CRF中，标签$x$的能量为

$$
E(x)=\sum _i\theta_i(x_i)+\sum _{ij}\theta_{ij}(x_i,x_j)
$$

- $\theta_i(x_i)$是一元能量，表示像素$i$被分割成$x_i$的能量，二元能量$\theta_{ij}(x_i,x_j)$像素点$i$、$j$同时分割成$x_i$、$x_j$的能量。
- 一元能量使用FCN的输出

$$
\theta_i(x_i) = -logP(x_i)
$$

- 二元能量表达式为

$$
\theta_{ij}(x_i, x_j)=\mu(x_i, x_j)[\omega_1exp(-\frac{\left \|p_i-p_j  \right \|^2} {2\sigma_\alpha^2}-\frac{\left \|I_i-I_j  \right \|^2}{2\sigma_\beta^2})+\omega_2exp(-\frac{\left \|p_i-p_j  \right \|^2} {2\sigma_\gamma^2})]
$$

- 主要参考[这里](https://blog.csdn.net/junparadox/article/details/52610744)

# v2

- v2在v1的基础上增加了多感受野

![deeplabv2](/images/4478311.jpg)

- 参考[这里](https://blog.csdn.net/ming0808sun/article/details/78843471)
