---
title: caffe运行顺序
tags:
  - caffe
  - cpp
categories: 
  - cpp
  - caffe
date: 2019-02-09 10:09:07
---

# blob
- explict，显示构造函数，只对构造函数有用，用来抑制隐式转换
```cpp
class String {
    explicit String ( int n ); // 本意是预先分配n个字节给字符串，加上explicit，就抑制了String ( int n )的隐式转换，
    String ( const char* p );  // 用C风格的字符串p作为初始化值
}
 
String s2 ( 10 );          //OK 分配10个字节的空字符串
String s3 = String ( 10 ); //OK 分配10个字节的空字符串
 
String s4 = 10;            //编译不通过，不允许隐式的转换
String s5 = 'a';           //编译不通过，不允许隐式的转换

class A {
    A(int a);   
};   
int Function(A a);   
// 当调用Function(2)的时候，2会隐式转换为A类型
    
class A {   
    explicit   A(int   a);   
};   
int Function(A a);  
// 这样，当调用Function(2)的时候，编译器会给出错误信息
```

- template
```cpp
// suppose I've declared
template <typename T> void foo(T& t);

template <> void foo<int>(int& t); 
// declares a specialization of the template, with potentially different body.

template void foo<int>(int& t); 
// causes an explicit instantiation of the template, but doesn't introduce a specialization. 
// It just forces the instantiation of the template for a specific type.
```

- iniline主要是将代码进行复制，扩充，会使代码总量上升，好处就是可以节省调用的开销，能提高执行效率

- shared_ptr引用计数智能指，可以参考[这里](https://blog.csdn.net/Xiejingfa/article/details/50750037)

# caffe.cpp

- step1: 命令行下输入./build/tools/caffe train -solver xxx.prototxt 运行了程序的入口caffe.cpp main()
- step2: caffe.cpp main()根据命令行输入的参数train 调用caffe.cpp train()
- step3: caffe.cpp train()读取xxx.prototxt的参数 调用solver.cpp Solver()的构造函数创建Solver对象
- step4: 创建Solver对象的时候需要调用solver.cpp Init()函数来初始化模型的网络
- step5: solver.cpp Init()函数调用solver.cpp InitTrainNet()和InitTestNets()函数来分别初始化训练和测试网络。
- step6: InitTrainNet() 通过xxx.prototxt 指定的xxxnet.prototxt读取net的参数，调用net.cpp Net()的构造函数，创建训练网络，
- step7: net.cpp Net()调用net.cpp Init()函数，通过for循环来1)创建网络中每一个Layer对象，2)设置bottom和top，3）调用layer.cpp Setup()，Setup()里会调用具体layer的LayerSetUp()和Reshape()
- step8: 调用InitTestNets()创建测试网络，与InitTrainNet(）类似
- step9: 运行返回到caffe.cpp train()中，利用创建好的solver对象调用solver.cpp Solve()函数
- step10: solver.cpp Solve() 调用 solver.cpp Step()函数，while循环迭代的次数，每次迭代 1）调用net.cpp ForwardBackward()来前向以及后向传播 2)solve.cpp ApplyUpdate()更新参数 3）每一定轮次运行solver.cpp TestAll()

- caffe.cpp中的main()调用train()，train()中创建solver对象，solver对象初始化会调用solver.cpp中的Init()
- Init()中，创建InitTrainNet()和InitTestNet()
- 返回到caffe.cpp的train()中，调用Solver()来训练网络，具体过程在solver.cpp的Step()中实现

- 以上抄自[这里](https://blog.csdn.net/BVL10101111/article/details/74787586 )

# layer_factory

- \#表示：对应变量字符串化  
- \#\#表示：把宏参数名与宏定义代码序列中的标识符连接在一起，形成一个新的标识符
- 连接符#@：它将单字符标记符变换为单字符，即加单引号。例如`#define B(x) #@x`，则B(a)即'a'，B(1)即'1'
```c++
#include <cstdio>  
#define trace(x, format) printf(#x " = %" #format "\n", x)  
#define trace2(i) trace(x##i, d) 
 
int main(int argc, char* argv[])
{
	int i = 1;
	char *s = "three";  
	float x = 2.0;
 
	trace(i, d);    // i = 1   
	trace(x, f);    // x = 2.000000
	trace(s, s);    // s = three      

	int x1 = 1, x2 = 2;  
	trace2(1);      // x1 = 1
	trace2(2);      // x2 = 2		
 
	return 0;
}
```
- 看[这里](https://www.jianshu.com/p/191f6cb3c102)吧，我太懒了。