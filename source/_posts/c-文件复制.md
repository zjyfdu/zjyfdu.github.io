---
title: c++文件复制
typora-root-url: ../../source
date: 2018-07-03 14:24:44
categories: cpp
---

```c
#include<iostream>
#include<fstream>
#include<cstring>

using namespace std;

int main(int argc, char* argv[])
{
	using namespace std;
	if (argc < 3){
		cout << "filename missed" << endl;
		return 0;
	}
	ifstream in(argv[1], ios::binary | ios::in);
	if (!in){
		cout << "source file open failed" << endl;
		return 0;
	}
	ofstream out(argv[2], ios::binary | ios::out); //打开文件用于写
	if (!out) {
		cout << "New file open error." << endl;
		in.close(); //打开的文件一定要关闭
		return 0;
	}
	if (strcmp(argv[1], argv[2])==0) {
		cout << "the src file can't be same with dst file" << endl;
		exit(EXIT_FAILURE);
	}
	char buf[2048];
	while (in)
	{
		//read从in流中读取2048字节，放入buf数组中，同时文件指针向后移动2048字节
		//若不足2048字节遇到文件结尾，则以实际提取字节读取。
		in.read(buf, 2048);
		//gcount()用来提取读取的字节数，write将buf中的内容写入out流。
		out.write(buf, in.gcount());
	}
	//char c;
	//while (in.get(c)){
	//	out.put(c);
	//}
	in.close();
	out.close();
}
```
