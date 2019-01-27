---
title: flask部署：gunicorn和nginx安装记录
date: 2018-01-14 14:14:42
tags: flask
categories: flask网站总结
---

### 1. gunicorn
python用的是anaconda 2.7，首先安装虚拟环境
好像是anaconda下用virtualenv会有点问题
gunicorn的w表示开启进程数
PS: [nohup的详细解释](http://www.ruanyifeng.com/blog/2016/02/linux-daemon.html) 
```
conda create -n newenv python=2.7 
source activate newenv //启用python 虚拟环境
pip install gunicorn //安装gunicorn
nohup gunicorn -w 4 --access-logfile access.log --error-logfile error.log -b 127.0.0.1:8080 manage:app&
app_file_name:app_name & 
```
gunicorn更改log的输出，[详细说明](http://docs.gunicorn.org/en/latest/settings.html#logging)
```
--access-logfile FILE
--error-logfile FILE, --log-file FILE
```
### 2. nginx
```
yum install nginx
```
然后修改nginx配置，转发至localhost的端口
```
server {
    listen       80 default_server;
    server_name  _;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```
检查nginx config，重启nginx
```
nginx -t
service naginx restart
```

### 3.nginx反向代理和防盗链

为了防止静态资源被其他站点请求，改为`return 403`。
但这样一来，本站请求的静态资源在经过static后，不再做转发，所以又把转发重复了一遍。
不知道有没有更优雅的写法。
```
server {
    listen       80 default_server;
    server_name  _;

    location /static/ {
        valid_referers 47.95.193.53;
        if ($invalid_referer) {
            return 403;
        }
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```
反爬虫
```
 location / {
        if ($http_user_agent ~* "python|curl|java|wget|httpclient|okhttp") {
            return 503; #service unavaiable
        }
        # 正常处理
        ...
    }
```

### 4.坑比阿里云的smtp端口

阿里云默默地把smtp的25端口禁掉了，要使用ssl的465端口
使用`flask-mail`需要在`config.py `中配置
```
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
```
