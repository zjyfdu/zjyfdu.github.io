---
title: BLEU和GLUE
tags:
  - 乱感叹
categories: 发疯文学
typora-root-url: ../../source
date: 2025-06-02 23:03:26
---
攒了好多年的问题了，该了结一下了。


# BLEU 机器翻译指标

transormer那篇论文里提到了BLEU指标，但一直不知道这个指标是啥。

BLEU（Bilingual Evaluation Understudy），通过比较机器翻译的结果与**参考译文**之间的相似度来衡量翻译质量。

$$
BLEU=BP*exp(\sum_{n=1}^N\frac{1}{N}logP_n)
$$

- N取4，即最多4-gram

- BP（Brevity Penalty）是长度惩罚因子，$l_c$代表表示机器翻译译文的长度，$l_s$表示参考答案的有效长度，避免机器翻译太短，hack了$P_n$指标，本质上还是$P_n$只考虑了准确率，没考虑召回率。
  $$
  BP = \begin{cases}
  1 & l_c \ge l_s \\
  exp(1-\frac{l_c}{l_s}) & l_c < l_s
  \end{cases}
  $$
  
- $P_n$，n-gram，比较译文和参考译文之间n组词的相似的占比。

比较详细的可以参考[这里](https://www.cnblogs.com/by-dream/p/7679284.html)。



# GLUE

GLUE（General Language Understanding Evaluation）是一个综合性的GLU（自然语言理解）评估基准，通过9个英语任务测试模型的通用能力，取平均值。


- 单句分类任务‌

  - CoLA‌：纽约大学发布的有关语法的数据集，该任务主要是对一个给定句子，判定其是否语法正确，因此CoLA属于单个句子的文本二分类任务
  - SST（情感分析）：是斯坦福大学发布的一个情感分析数据集，主要针对电影评论来做情感分类，因此SST属于单个句子的文本分类任务（SST-2是二分类，SST-5是五分类，SST-5的情感极性区分的更细致）
- 相似性任务‌

  - MRPC/QQP‌（句子对语义等价判断）：判断两个给定句子，是否具有相同的语义，属于句子对的文本二分类任务
  - STS-B‌（句子相似度评分）：用1到5的分数来表征两个句子的语义相似性，本质上是一个回归问题，但依然可以用分类的方法做，因此可以归类为句子对的文本五分类任务
- 推理任务‌

  - MNLI/QNLI/RTE/WNLI‌（文本蕴含与推理）
    

也是比较老的指标了，BERT、T5那个时代的。