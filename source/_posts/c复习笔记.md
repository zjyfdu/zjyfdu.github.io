---
title: c复习笔记
date: 2018-03-11 22:09:11
tags:
  - cin/cout
  - lambda
  - 构造函数
categories: cpp
---

- cin 带空格的字符串时，需要这样`cin.getline(s, 80)`，s是char数组
- 或者也可以这样`getline(cin, str)`，原型为`istream& getline (istream& is, string& str); `

- cout 控制输出精度 `cout << fixed << setprecision(2) << f`，`#include <iomanip>`
- cout 控制输出格式`cout << setfill('0') << setw(4) << a[i][j]`
- lambda表达式
![](http://ot0uaqt93.bkt.clouddn.com/18-7-3/10535321.jpg "lambda!") 

- 使用lambda对vector进行排序

```
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
```
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