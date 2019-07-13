---
title: 优秀的Typora
tags:
  - caffe
  - docker
categories: cpp
typora-root-url: ../../source
date: 2019-07-14 00:22:33
---

今天意外地发现了[Typora](https://typora.io/)，几乎解决了我关于记笔记和写博客的所有问题。

# 1.日常记笔记

其实我大概三个月前是用纸笔记笔记的，直到我意识到我打字已经比写字快很多了。。。

然后我开始用word记事，当然是可以的，但是总觉得不够轻便

然后我开始用onenote，但功能又太少了，关键时刻连个公式都没有



直到今天，直到今天我发现了Typora

1. 实现了markdown的所见所得，标题、加粗、插图，可以直接显示，实现了word的功能又不用频繁点鼠标。
2. 公式可以直接用$\LaTeX{}$打啊，而且边写边预览！
3. 可以直接贴代码啊，直接语法高亮啊！这个用word我是不会做的。
4. 装了pandoc之后，**能直接导出word**，而且公式还是原生的word公式，不是mathtype的！

其实看了上面的功能，我就怀疑这个软件像是一个本地版的hexo，然后我在GitHub上找，没找到源码，但找到了到了Typora的组织，里面的仓库有node、有electron，emmm，我更加怀疑了🤔

# 2.Hexo

所以把Typora当作Hexo的客户端非常合适，好像Hexo写博客难受的几个点都可以解决了。

## 2.1实时预览

hexo里能实现的，Typora上也都能实现，所以其实就是实现了实时预览。

虽然理论上也可以开`hexo server`，但是毕竟还是要到浏览器里刷新一下才能看到变化的，比不上直接用这个来得直接。

## 2.2图片粘贴

贴图简直是hexo的灾难，最早我是把图传到七牛云的，然后复制了链接再手动写到博客里。

后来七牛云突然就不允许外链了，差点把我的图都搞丢，吃了教训之后，我把图都放到了`source/images`里，然后在贴图的时候用`![](/images/ctc.jpg)`，图片是要自己复制的，路径也是要自己写的。

但是现在有Typora 了！可以实现图片直接粘贴了

设置好图片自动复制，不管是本地图片，还是网络图片，都复制到`source/images`，显示相对路径，同时需要设置图片根目录，

```yaml
typora-root-url: ../../source
```

这样Typora生成的相对路径才可以正常在网站上显示。

![屏幕快照 2019-07-14 上午1.15.21](/images/屏幕快照 2019-07-14 上午1.15.21-3039456.png)

但mac上好像不能批量设置图片根目录，所以修改默认的post配置，在`scaffolds\post.md`里，添加上面那一句。

以前写的博客没有这一句怎么办呢？我弄了半天的`sed`最终放弃了（mac的freebsd上的sed和gnu的sed不一致），还是用python一把梭

```python
import os

path_root = './_posts/'
files = os.listdir(path_root)
files = [path_root + x for x in files if x.endswith('.md')]
insert_line = 'typora-root-url: ../../source'

for file in files:
    with open(file) as f:
        lines = f.readlines()

    if any([insert_line in x for x in lines]):
        continue

    lines.insert(2, insert_line + '\n') // 在哪一行插入都行
    with open(file, 'w') as f:
        f.writelines(lines)
```

##2.3一个没解决的图片问题

后来想到还有一个问题没有解决，图片直接用的是原图，没有做裁剪和重命名。

参考[这里](https://www.karlzhou.com/articles/compress-minify-hexo/)做的，用`gulp`压缩图片。

在`package.json`的 `dependencies`里加入

```json
"del": "^2.2.2",
"gulp": "^3.9.1",
"gulp-clean-css": "^2.3.2",
"gulp-htmlclean": "^2.7.22",
"gulp-htmlmin": "^3.0.0",
"gulp-imagemin": "^3.4.0",
"gulp-uglify": "^2.1.2",
```

然后，

```shell
cnpm insall
cnpm update # 直接install后报错，update之后好了
cnpm audit fix
```

`gulpfile.js`太长不贴了，原网站里有

```
gulp build && hexo d
```

这个时候电脑嗡嗡作响，整个build花了6min，以后图越多会越慢的，