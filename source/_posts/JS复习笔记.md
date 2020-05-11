---
title: JS复习笔记
typora-root-url: ../../source
date: 2018-01-01 18:25:23
tags:
  - javaScript
  - 复习笔记
categories: flask网站总结
---

1. 有两种比较运算符：
==，自动转换数据类型再比较，会得到非常诡异的结果
===，如果数据类型不一致，返回false，如果一致，再比较
2. `NaN === NaN; // false`
唯一能判断NaN的方法是通过isNaN()函数
`isNaN(NaN); // true`
3. 浮点数比较要这样
`Math.abs(1 / 3 - (1 - 2 / 3)) < 0.0000001; // true`
4. 并如果一个变量没有通过var申明就被使用，就自动被申明为全局变量
ECMA在后续规范中推出了strict模式，需要在第一行加入
`'use strict';`
5. 最新的ES6标准新增了一种多行字符串的表示方法，用反引号 \` ... \` 表示：
还有模版字符串
```
var name = '小明';
var age = 20;
var message = `你好, ${name}, 你今年${age}岁了!`;
alert(message);
```
6. `for ... of`ES6引入
`for ... in`循环由于历史遗留问题，它遍历的实际上是对象的属性名称。
更推荐用`forEach`
```
array1.forEach(function (element, index, array) {
    // element: 指向当前元素的值
    // index: 指向当前索引
    // array: 指向Array对象本身
    console.log(element + ', index = ' + index);
});

set1.forEach(function (element, sameElement, set) {
map1.forEach(function (value, key, map) {
```

7. `augments`和`rest`（ES6引入）
```
function foo(a, b) {
    var i, rest = [];
    if (arguments.length > 2) {
        for (i = 2; i<arguments.length; i++) {
            rest.push(arguments[i]);
        }
    }
    console.log('a = ' + a);
    console.log('b = ' + b);
    console.log(rest);
}

function foo(a, b, ...rest) {
    console.log('a = ' + a);
    console.log('b = ' + b);
    console.log(rest);
}

foo(1, 2, 3, 4, 5);
// 结果:
// a = 1
// b = 2
// Array [ 3, 4, 5 ]

foo(1);
// 结果:
// a = 1
// b = undefined
// Array []
```
8. 变量提升
JavaScript的函数定义有个特点，它会先扫描整个函数体的语句，把所有申明的变量“提升”到函数顶部
```
function foo() {
    var
        x = 1, // x初始化为1
        y = x + 1, // y初始化为2
        z, i; // z和i为undefined
    // 其他语句:
    for (i=0; i<100; i++) {
        ...
    }
}
```
1. 默认有一个全局对象window，全局作用域的变量实际上被绑定到window的一个属性
2.  为了解决块级作用域，ES6引入了新的关键字let，用let替代var可以申明一个块级作用域的变量：
```
'use strict';

function foo() {
    var sum = 0;
    for (let i=0; i<100; i++) {
        sum += i;
    }
    // SyntaxError:
    i += 1;
}
```
11. ES6标准引入了新的关键字const来定义常量，const与let都具有块级作用域
12. 要保证`this`指向正确，必须用`obj.xxx()`的形式调用！
```
'use strict';

var xiaoming = {
    name: '小明',
    birth: 1990,
    age: function () {
        var that = this; // 在方法内部一开始就捕获this
        function getAgeFromBirth() {
            var y = new Date().getFullYear();
            return y - that.birth; // 用that而不是this
        }
        return getAgeFromBirth();
    }
};

xiaoming.age(); // 25
var tmp = xiaoming.age;
tmp(); //NaN
```
13. 用 `apply`或`call`传`this`
call和apply作用是一样的，都是为了改变某个函数运行时的上下文（context）而存在的，换句话说，就是为了改变函数体内部this的指向
从[这里](https://www.jianshu.com/p/aa2eeecd8b4f)抄的
```
Math.max.apply(null, [3, 5, 4]); // 5
Math.max.call(null, 3, 5, 4); // 5
```
1.  名字空间
```
// 唯一的全局变量MYAPP:
var MYAPP = {};

// 其他变量:
MYAPP.name = 'myapp';
MYAPP.version = 1.0;

// 其他函数:
MYAPP.foo = function () {
    return 'foo';
};
```
15. 服务器在设置Cookie时可以使用`httpOnly`，设定了`httpOnly`的Cookie将不能被JavaScript读取。这个行为由浏览器实现，主流浏览器均支持`httpOnly`选项，IE从IE6 SP1开始支持。
16. 原生js获取children
```
// 获取节点test下的所有直属子节点:
var cs = test.children;

// 获取节点test下第一个、最后一个子节点：
var first = test.firstElementChild;
var last = test.lastElementChild;
```
17. CSS允许`font-size`这样的名称，但它并非JavaScript有效的属性名，所以需要在JavaScript中改写为驼峰式命名`fontSize`
```
// 获取<p id="p-id">...</p>
var p = document.getElementById('p-id');
// 设置CSS:
p.style.color = '#ff0000';
p.style.fontSize = '20px';
p.style.paddingTop = '2em';
```
18. 一种是修改`innerHTML`属性，这个方式非常强大，不但可以修改一个DOM节点的文本内容，还可以直接通过HTML片段修改DOM节点内部的子树。
修改`innerText`或`textContent`属性，这样可以自动对字符串进行HTML编码，保证无法设置任何HTML标签。两者的区别在于读取属性时，innerText不返回隐藏元素的文本，而textContent返回所有文本。
innerHtml
19. 没有name属性的`<input>`的数据不会被提交。
```
<!-- HTML -->
<form id="login-form" method="post" onsubmit="return checkForm()">
    <input type="text" id="username" name="username">
    <input type="password" id="input-password">
    <input type="hidden" id="md5-password" name="password">
    <button type="submit">Submit</button>
</form>

<script>
function checkForm() {
    var input_pwd = document.getElementById('input-password');
    var md5_pwd = document.getElementById('md5-password');
    // 把用户输入的明文变为MD5:
    md5_pwd.value = toMD5(input_pwd.value);
    // 继续下一步:
    return true;
}
</script>
```
20. 这是因为浏览器的同源策略导致的。默认情况下，JavaScript在发送AJAX请求时，URL的域名必须和当前页面完全一致。
完全一致的意思是，域名要相同（www.example.com和example.com不同），协议要相同（http和https不同），端口号要相同（默认是:80端口，它和:8080就不同）。有的浏览器口子松一点，允许端口不同，大多数浏览器都会严格遵守这个限制。
21. 解决跨域请求的几种方法：Flash、同源服务器转发、JSONP、CORS
下面谈的都是CORS。跨域能否成功，取决于对方服务器是否愿意给你设置一个正确的Access-Control-Allow-Origin，决定权始终在对方手中
上面这种跨域请求，称之为“简单请求”。简单请求包括GET、HEAD和POST（POST的Content-Type类型
仅限application/x-www-form-urlencoded、multipart/form-data和text/plain），并且不能出现任何自定义头（例如，X-Custom: 12345），通常能满足90%的需求。
对于PUT、DELETE以及其他类型如application/json的POST请求，在发送AJAX请求之前，浏览器会先发送一个OPTIONS请求（称为preflighted请求）到这个URL上，询问目标服务器是否接受。
22. 
```
getElementById
getElementsByTagName
getElementsByClassName

innerHTML //可以插入DOM
innerText //会HTML编码
```

