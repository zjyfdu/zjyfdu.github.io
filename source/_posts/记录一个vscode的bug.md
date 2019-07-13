---
title: 记录一个vscode的bug
typora-root-url: ../../source
tags:
  - vscode
date: 2018-08-08 00:53:58
---
# 啰嗦一下

- 在mac下，使用vscode，使用汉字输入法，删除完后，会多一个退格符！而且这个退格符默认是不可见的！
- 过年在家写论文的时候，就发现xetex模型奇妙不能编译，说是多了字符，苦于不知道这个字符是啥，也不知道怎么描述这个现象，一直没有找到原因。
- 就在今天，我配置博客的搜索的时候，又被这个bug给搞了，看别人的解释说是生成的检索文件里，多了BS(unicode)这个字符，终于顺着这个BS，我找到了困扰我半年的bug。
- 十分激动，以至于我一改性冷淡的文风，在大半夜里啰嗦这么多。

# vscode并不打算修

- 参考了[这里](https://juejin.im/entry/5a806ddef265da4e84092eeb)的说明。
> vscode底层使用了electron，这是electron的bug，electron不解决这个问题，vscode就不会解决。
> electron底层使用了chromium， 这是chromium的bug，chromium不解决，elctron就无法解决。
- 非常稳，于是[这个bug还是open的](https://github.com/Microsoft/vscode/issues/37114)。

# 补救措施

- 首先让这个字符显示出来

```json
"editor.renderControlCharacters": true
```

- 使用插件 Remove backspace control character，并如下配置，这样在保存文件的时候，会自动帮你删除这些控制符

```json
“editor.formatOnSave”: true 
```
