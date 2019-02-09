---
title: grep中的正则表达式
tags:
  - 正则
  - grep
date: 2018-11-20 19:36:53
---

照抄的[这里](https://blog.csdn.net/yufenghyc/article/details/51078107)

# 正则表达式
- 基础正则，basic regex，即bres
- 扩展正则，extended regex，即eres
- perl的正则，perl regex，即pres

# 不同正则表达式的区别
- bres需要多写转义
```shell
\{n,m\}, x\|y #bres需要写转义，
{n,m}, x|y    #而eres和pres不需要
```
- pres可以用```\d, \D, \S, \s```，其它两种不可以。

# grep
- 默认的正则为基础正则，"-E"表示eres，"-P"表示pers.
- egrep等效于grep -E，egrep -P等效于 grep -P

# sed
- 默认是eres，-r表示要用eres，不支持pres
- mac下到sed和linux还不太一样，写inplace替换要这样，其中，`-i`后面是

```shell
sed -i '' 's/http.*ot0uaqt93.bkt.*\//\/images\//g' `ls *.md`
```

# awk
- 厉害了，只支持eres
