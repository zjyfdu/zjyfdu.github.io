---
title: write a shell in c
typora-root-url: ../../source
tags:
  - caffe
  - docker
categories: cpp
date: 2018-07-16 15:06:39
---

源文章标题取得很大，[write a shell in c](https://brennan.io/2015/01/16/write-a-shell-in-c/)。相关的内容总结如下。

- fork(), exec() and waitpid() are defined by the POSIX standard, and Windows is not POSIX-compliant. In order to have POSIX compliance under Windows, you should compile under Cygwin.

- fork, exec, chdir are in unistd.h(unix std); execvp is in stdlib

- system命令相当于 fork + exec + waitpid

- windows也提供了一个chdir函数，叫_chdir，在direct.h里

- cc来自于Unix的c语言编译器，是 c compiler 的缩写。gcc来自Linux世界，是GNU compiler collection 的缩写，注意这是一个编译器集合，不仅仅是c或c++

- strtok()
```c
char sentence[]="192.168...9...14";
char *token=strtok(sentence,".");
while(token!=NULL){
  cout<<token<<" ";
  token=strtok(NULL,".");
}
```

- 在gcc编译器中，对标准库进行了扩展，加入了一个getline函数。会自动malloc, realloc，所以用的话，需要自己手动free，好像没啥人用，参考[这里](https://www.cnblogs.com/xkfz007/archive/2012/08/01/2618366.html)

- 我用system代替了fork等，于是有了[window版](https://github.com/zjyfdu/lsh/blob/master/src/%E6%BA%90.cpp)
