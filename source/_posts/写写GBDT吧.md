---
title: GBDT和xgboost
tags:
  - gbdt
  - xgboost
categories: 推荐
typora-root-url: ../../source
date: 2024-04-13 12:05:02
---

> 在浮躁的LLM时代，仍然坚持古法建模，致敬xgb匠人

# 单棵树

- ID3 算法中根据特征选择和信息增益评估，每次选择信息增益最大的特征作为分支标准
- C4.5 使用“增益率”（gain ratio）来选择最优的分支标准
- CART 的分支标准建立在 GINI 指数上，GINI 值越大表明样本集合的类别越杂乱

# GBDT
- 先有BT（boosting tree）（相比随机森林是stacking）
- 随后有了GBT，gradient boosting tree，又可分为GBDT和GBRT，分类数和回归树
- 核心思想是**利用损失函数的负梯度在当前模型的值作为残差的近似值**，本质上是对损失函数进行一阶泰勒展开，从而拟合一个回归树

$$
L(y,f_t) = L(y,f_{t-1}+h_t)=L(y,f_{t-1})+\frac{\partial L(y, f_{t-1})}{\partial f_{t-1}}h_t
$$

- 对于mse loss，$\Delta L=L(y,f_t)-L(y,f_{t-1})=\frac{\partial L(y, f_{t-1})}{\partial f_{t-1}}h_k$ ，所以$h_k=-\frac{\partial L(y, f_{t-1})}{\partial f_{t-1}}$，负梯度也就是残差
- 对于log loss，[我没看懂](https://zhuanlan.zhihu.com/p/388225723)

# xgboost

> 主要<del>参考</del>自[这里](https://juejin.cn/post/6963993583217016869)，[原论文](https://arxiv.org/pdf/1603.02754.pdf)

然后才进化出了xgb，有几个改进点
  - 加了正则项，包含树的节点数，权重
  - 一阶泰勒变成了二阶
  - 一些实现上的优化，缺失值、分裂点

损失函数定位为：
$$
L = \sum_il(f_i,y_i)+\sum\Omega(f) \\
\Omega(f)= \gamma T+\frac{1}{2}\lambda \lVert \omega \rVert ^2
$$
$\Omega$中，$T$表示节点个数，$\omega$表示叶子节点的值，loss里直接包含了正则想，相比GBDT更不同意过拟合

对$L$进行二阶展开，
$$
L=\sum_i[l(y_i,f_i^{t-1})+g_if_i^t+\frac{1}{2}h_i(f_i^t)^2]+\sum\Omega(f)
$$
这里$g_i=\frac{\partial l(y_i,f_i^{t-1})}{\partial f_i^{t-1}}$，$h_i=\frac{\partial ^2 l(y_i,f_i^{t-1})}{\partial ^2 f_i^{t-1}}$，即$l(y_i,f_i^{t-1})$对$ f_i^{t-1}$的一阶导数和二阶导数。利用泰勒展开式，这里将损失函数转化成了一个二次函数，而且这里二次项的系数为正，可以很方便的求得函数的最小值

简单一点，相对于$ f^{t}$是常数项的部分去掉
$$
L=\sum_i[g_if_i^t+\frac{1}{2}h_i(f_i^t)^2]+\sum\Omega(f^t)
$$
决定$ f^{t}$的主要是两个纬度，一是这颗树的形态，二是树的叶子节点的权重。这里用数学表达式来表示就是
$$
\sum_if_i^t=\sum_{j=1}^T\sum _{i\in I_j} \omega_j
$$
等式左边的意义很明显，就是所有样本在第$t$棵树上输出的和，等式右边用另一种方式表达了这个值，第一个求和符号表示所有的叶子节点，第二个求和符号表示被分到每个叶子节点的样本集合，$i\in I_j$表示被分到第$j$个叶子节点的样本集合。$\omega_j$代表第$j$个叶子节点的权重。可以这么理解，样本分到哪一个叶子节点上表示了树的结构。

把这个细化的表达式带入到泰勒展开近似的损失函数中得到，
$$
L=\sum_{j=1}^T[(\sum _{i\in I_j} g_i)\omega_j+\frac{1}{2}(\sum _{i\in I_j}h_i+\lambda)\omega_j^2]+\gamma T
$$
给定树的结构下
$$
\omega_j^*=\frac{\sum _{i\in I_j} g_i}{\sum _{i\in I_j}h_i+\lambda}
$$


那么怎么确定树的结构呢？

答案是枚举，在一个节点那里想要做分裂节点的操作，哪些样本要分到左边，哪些节点要分到右边，XGBoost就把所有的样本按某个特征排序，然后切分，以此确定树的结构，枚举下来算出最小损失值，就作为最优结构。

实现上的一些优化：

- 对每个特征的分割决策使用并行策略：首先把每个特征都排序，因为对特征在不同的位置进行分割是独立的，所以可以使用并行的线程进行计算，从而加速训练的速度。

- 梯度数据缓存策略：会把需要的梯度数据放到一个额外的内存里，使用预取和缓存的方式来提高缓存的命中率，从而提升数据IO的速度。

- 去中心化内存策略：为了实现去中心化的计算，将数据分割成不同的块，然后将所有块存储在磁盘上。在计算过程中，利用一个单独的线程来预取磁盘中的数据，保证运算和取数据可以同时发生。