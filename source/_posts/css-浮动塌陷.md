---
title: css 浮动塌陷
date: 2018-01-30 14:25:26
categories: flask网站总结
---

[来自这里](http://blog.csdn.net/chris_z_0622/article/details/65442975)
css 子元素设置为float之后，脱离文件流，导致父元素撑不起来，解决办法
1. 父元素也设置为float（不推荐，会影响父元素后面都元素）
2. 父元素添加 overflow:hidden（诡异的css）
3. 建立一个空的子div `<div style="clear: both"></div>`
4. 通过伪类:after清除浮动，具体如下
```html
<div class="father">
    <div class="son">子元素</div>
</div>
```
```
.son {
    float: left;
}
.father:after {
    content: "";
    height: 0;
    width: 0;
    visibility: hidden;
    clear: both;
    display: block;
}
```