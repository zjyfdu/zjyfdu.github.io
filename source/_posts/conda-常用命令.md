---
title: conda 常用命令
tags:
  - conda
  - python
categories: python
date: 2018-11-19 18:52:16
---
1. 创建虚拟环境

```shell
conda create -n your_env_name python=x.x anaconda
```

最后的anaconda可选，有的话，会安装很多包，numpy、sklearn等等

2. 激活

```shell
source activate your_env_name
```

3. 安装包

```shell
conda install -n your_env_name [package]
```

4. 不激活

```shell
source deactivate
```

5. 已经有的虚拟环境

```shell
conda env list
```

6. 删除虚拟环境

```shell
conda remove -n your_env_list -all
```

7. 检查conda是否安装

```shell
conda -v
```

8. 更新conda

```shell
conda update conda
```