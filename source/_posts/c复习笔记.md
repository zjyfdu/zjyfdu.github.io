---
title: c复习笔记
typora-root-url: ../../source
date: 2018-03-11 22:09:11
tags:
  - cin/cout
  - lambda
  - 构造函数
categories: cpp
---

- cin 带空格的字符串时，需要这样`cin.getline(s, 80)`，s是char数组
- 或者也可以这样`getline(cin, str)`，原型为`istream& getline (istream& is, string& str); `，C++对每种流都定义了一个getline函数
- 在gcc编译器中，对标准库进行了扩展，加入了一个getline函数。会自动malloc, realloc，所以用的话，需要自己手动free，好像没啥人用，参考[这里](https://www.cnblogs.com/xkfz007/archive/2012/08/01/2618366.html)

- cout 控制输出精度 `cout << fixed << setprecision(2) << f`，`#include <iomanip>`
- cout 控制输出格式`cout << setfill('0') << setw(4) << a[i][j]`
- [更多](https://blog.csdn.net/yockie/article/details/9104899)

- cin cout 重定向
```cpp
freopen("foo.txt","w",stdout); 
freopen(“bar.txt”,”r”,stdin);
```

- lambda表达式
![](/images/10535321.jpg "lambda!") 

- 使用lambda对vector进行排序
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

int main()
{
   int n;
   double th;
   cin >> n >> th;
   vector<pair<string, double>> res;  
   while(n--){
        string name;
        double score;
        cin >> name >> score;
        if(score > th){
            res.push_back(pair<string, double>(name, score));
        }
    }
    sort(res.begin(), res.end(), [](pair<string, double>& a, pair<string, double>& b) {return a.second > b.second;});
    for(auto i: res){
        printf("%s %.1f\n", i.first.c_str(), i.second);
    }
   return 0;
}
```

- erase删除vector元素
```cpp
for(it=iVec.begin();it!=iVec.end();){
　　if(*it==4 || *it==5)
　　　　it=iVec.erase(it);
　　else
　　　　it++;
}
```

- `Sample a(0)`, `Sample a = 0`, 都是调用构造函数
- `Sample a(9); a = 8` 调用两次构造函数，
- `Sample b = a `, `Sample b(a)` 拷贝构造函数
- 类型转换构造函数，编译系统会生成一个临时变量


- C++编译器遵循以下优先顺序:
> 先找参数完全匹配的普通函数(非由模板实例化而得的函数)，再找参数完全匹配的模板函数，再找实参经过自动类型转换后能够匹配的普通函数，上面的都找不到, 则报错。

- 优雅的内存对齐方法
```c
unsigned int calc_align(unsigned int n, unsigned align)
{
    return ((n + align - 1) & (~(align - 1)));
}
```

- __declspec(dllexport)是导出声明，说明这个函数要从DLL中导出给别人用。
- __declspec(dllimport)是说这个函数是从别处导入的，不适用也能正常编译代码。

