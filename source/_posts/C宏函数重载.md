---
title: C宏函数重载
tags: cpp
categories: cpp
date: 2019-02-14 17:46:37
---

- 理论上，宏函数是不能重载的，第二个宏会直接覆盖掉第一个
- 但我今天看到了一个非常~~sao~~优雅的方法，可以功能上实现重载，原文在[这里](https://blog.csdn.net/lmhuanying1012/article/details/78715351)

```cpp
#define OneArgument(a) // ...action with one argument
#define TwoArguments(a, b) // ...action with two arguments
 
#define GetMacro(_1, _2, NAME, ...) NAME
#define Macro(...) GetMacro(__VA_ARGS__, TwoArguments, OneArgument, ...)(__VA_ARGS__)
 
// usage:
Macro(a); // OneArument(a) is called
Macro(a, b);  // TwoArguments(a, b) is called
```
- 其中，`__VA_ARGS__`是参数`...`的展开

- 以此类推，三个参数的重载也是能实现的

```cpp
#define OneArgument(a) // ...action with one argument
#define TwoArguments(a, b) // ...action with two arguments
#define ThreeArguments(a, b, c) // ...action with three arguments
 
#define GetMacro(_1, _2, _3, NAME, ...) NAME
#define Macro(...) GetMacro(__VA_ARGS__, ThreeArguments, TwoArguments, OneArgument, ...)(__VA_ARGS__)
 
// usage:
Macro(a); // OneArument(a) is called
Macro(a, b);  // TwoArguments(a, b) is called
Macro(a, b, c);  // ThreeArguments(a, b, c) is called
```
