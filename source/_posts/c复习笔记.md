---
title: c复习笔记
date: 2018-03-11 22:09:11
---

- cin 带空格的字符串时，需要这样`cin.getline(s, 80)`，s是char数组
- 或者也可以这样`getline(cin, str)`，原型为`istream& getline (istream& is, string& str); `

- cout 控制输出精度 `cout << fixed << setprecision(2) << f`，`#include <iomanip>`
- cout 控制输出格式`cout << setfill('0') << setw(4) << a[i][j]`

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

```
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<vector<int> > a(n, vector<int>(2));
    vector<int> resultx;
    vector<int> resulty;
    for (int i = 0; i < n; i++) {
        cin >> a[i][0] >> a[i][1];
    }
    int first = 0;
    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = 0; j < n; j++) {
            if (j == i)
                continue;
            if (a[j][0]>=a[i][0] && a[j][1]>=a[i][1]) {
                break;
            }else {
                count++;
            }
            if (count == n-1)//yes{
                resultx.push_back(a[i][0]);
                resulty.push_back(a[i][1]);
            }
        }
    }
    for(int i = 0; i < resultx.size()-1; i++){
        for (int j = i+1; j < resultx.size(); j++){
            if (resultx[i]>resultx[j]){
                int tmpx, tmpy;
                tmpx = resultx[i];
                resultx[i] = resultx[j];
                resultx[j] = tmpx;
                tmpy = resulty[i];
                resulty[i] = resulty[j];
                resulty[j] = tmpy;
            }
        }
    }
    cout << '(' << resultx[0] << ',' << resulty[0] << ')';
    for (int i = 1; i < resultx.size(); i++)
    {
        cout << ',' << '(' << resultx[i] << ',' << resulty[i] << ')';
    }
    cout << endl;
    return 0;
}
```