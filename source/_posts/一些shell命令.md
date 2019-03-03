---
title: 一些shell命令
tags: shell
categories: shell
date: 2019-01-23 19:20:03
---

- for循环

```shell
for file in `ls /etc`

for skill in Ada Coffe Action Java; do
    echo "I am good at ${skill}Script"
done

for (( EXP1; EXP2; EXP3 ))
do
    # do something
done

while condition
do
    # do something
done

until condition
do
    # do something
done

# while : 等效于 while true
```

- if

```shell
if condition
then
    # do something
elif
    # do something
else
    # do something
fi

if [ -e "$filename" ] # 文件是否存在，r、w、x是否可读、写、执行
                      # d是否为目录、f是否为文件
if [ $var -gt 0 ] # 还有lt、ge、le、eq、ne
```

- case

 ```shell
case "$varname" in
    [a-z]) echo "abc";;
    [0-9]) echo "123";; #还不知道为啥这么写，以后再补充吧
esac
 ```

- 文件包含

```shell
source ./function.sh
. ./function.sh
```

- 字符串

```shell
string="abcd"
echo ${#string} # 字符串长度

string="zhe pian tai shui le"
echo ${string:13:4} # shui
```

- 数组

```shell
arr=(1 2 3 4 5)
echo ${arr[3]}

echo ${#arr[@]} # 数组长度
echo ${arr[#arr[@]-1]} # 最后一个元素
```
- 问号，和C里面的问号一样

```shell
a=10
(( t=a<50?0:1 )) # t=0
```

- `/dev/null`是个空文件，清空一个文件可以用`cat /dev/null > tmp.log`，不想保存log，也不想输出到屏幕，可以`1>/dev/null 2>&1`
- 清空一个文件也可用`: > tmp.log`，:是个内建命令，什么也不做，永远返回0

```shell
:
echo $? # 0
 ```

 - `cp t.{txt,back}` 文件名扩展
 - 大括号和小括号的区别

 ```shell
 a=123
 (a=321)
 echo $a # 123 在子进程中修改了a的值，对当前进程没影响
 {a=321;}
 echo $a # 321 想当于是一个匿名函数
 ```

 - `sudo sh -c "..."`，引号里的内容都会有sudo权限
 - `echo $(( 2#101011 ))`，这里是2进制的意思
