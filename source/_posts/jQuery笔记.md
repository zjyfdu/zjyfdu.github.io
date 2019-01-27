---
title: jQuery笔记
date: 2018-02-25 11:29:08
tags:
  - javaScript
categories: flask网站总结
---

1. 按属性选取`var email = $('[name=email]');`
2. jQuery对象和DOM对象之间可以互相转化：
```
var div = $('#abc'); // jQuery对象
var divDom = div.get(0); // 假设存在div，获取第1个DOM元素
var another = $(divDom); // 重新把DOM包装为jQuery对象
```
3. 过滤器
```
$('ul.lang li'); // 选出JavaScript、Python和Lua 3个节点

$('ul.lang li:first-child'); // 仅选出JavaScript
$('ul.lang li:last-child'); // 仅选出Lua
$('ul.lang li:nth-child(2)'); // 选出第N个元素，N从1开始
$('ul.lang li:nth-child(even)'); // 选出序号为偶数的元素
$('ul.lang li:nth-child(odd)'); // 选出序号为奇数的元素
```
4. ajax jsonp
```
    $.ajax({
      type: 'get',
      url: "http://api.money.126.net/data/feed/0000001,1399001",
      dataType: 'jsonp',
      success: function(data) {
            var str = '当前价格：' +
                data['0000001'].name + ': ' +
                data['0000001'].price + '；' +
                data['1399001'].name + ': ' +
                data['1399001'].price;
            alert(str);
        },
      error: function() {
            alert('出错了');
        }
    });

```
jQuery的jqXHR对象类似一个Promise对象，我们可以用链式写法来处理各种回调
```
$.ajax({
      type: 'get',
      url: "http://api.money.126.net/data/feed/0000001,1399001",
      dataType: 'jsonp'
}).done(function (data) {
    ajaxLog('成功, 收到的数据: ' + JSON.stringify(data));
}).fail(function (xhr, status) {
    ajaxLog('失败: ' + xhr.status + ', 原因: ' + status);
}).always(function () {
    ajaxLog('请求完成: 无论成功或失败都会调用');
});
```
