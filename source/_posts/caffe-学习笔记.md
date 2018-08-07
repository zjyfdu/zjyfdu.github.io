---
title: caffe 学习笔记
date: 2018-01-11 01:46:30
tags:
  - caffe
  - 学习笔记
  - docker
categories: caffe
---

## 安装

### mac

直接看官网的安装有点抓不住要点，有一篇博客介绍得很详细，[点这里](http://akmetiuk.com/posts/2016-03-29-compiling-caffe.html)。是针对MAC下caffe及其python模块的安装，包括有哪些依赖、怎么编译，会遇到哪些坑，以及怎么解决坑等等。感谢作者！ 

### docker
docker就方便多了，需要先安装docker，centos照着[这一篇](https://www.liquidweb.com/kb/how-to-install-docker-on-centos-6/)

```bash
rpm -iUvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
yum update -y
yum -y install docker-io
service docker start
chkconfig docker on
```
至此docker安装完毕，然后搜索caffe的镜像。
```bash
docker search caffe
```
然后会搜到一堆镜像
```
NAME                                DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
tleyden5iwx/caffe-cpu-master                                                        48                   [OK]
bvlc/caffe                          Official Caffe images                           42                   [OK]
kaixhin/caffe                       Ubuntu Core 14.04 + Caffe.                      38                   [OK]
kaixhin/cuda-caffe                  Ubuntu Core 14.04 + CUDA + Caffe.               38                   [OK]
...
```
其中就有官方的docker，也不知道为什么，我就用了`kaixhin/caffe`
```bash
docker pull kaixhin/caffe
```
这个名字太丑了，我们改为
```bash
docker tag kaixhin/caffe caffe
```
然后
```bash
docker run -i -t caffe /bin/bash
```
然后就你直接用现成的caffe了。`exit`退出后，需要保存容器，不然下次还是会打开全新的容器。
```bash
docker ps -l
# CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES
# c8f1d7bcb4f2        caffe               "/bin/bash"         8 minutes ago       Exited (0) 7 minutes ago                       boring_turing
docker commit c8f caffe
```
还有其余一些docker命令
```
docker stop $(docker ps -a -q) #停用所有容器
docker rm $(docker ps -a -q) #删除所有容器
docker rmi <image id> #删除image
```

## MNIS
基本全是照着[这里](https://zhuanlan.zhihu.com/p/24110318)，一知半解地做

训练时，报错`Unknown database backend`，需要在`Makefile.config`中，修改`USE_LMDB := 1`，然后重新`make clean`，`make all -j4`等等
