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
```

- 文件包含

```shell
source ./function.sh
. ./function.sh
```

- 字符串

```shell
string="abcd"
echo ${#string}

string="zhe pian tai shui le"
echo ${string:13:4}  
```