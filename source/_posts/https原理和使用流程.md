---
title: https原理和使用流程
date: 2018-01-14 11:49:09
tags: https
categories: flask网站总结
---

### http原理
看[这里](https://www.cnblogs.com/xinzhao/p/4949344.html)

### 使用流程
1. 上[阿里云](https://www.aliyun.com/product/cas)或七牛云的免费ssl服务，阿里云不用填什么资料直接就审核了，七牛云好像麻烦一点。
2. 配置DNS
3. 审核通过之后，下载证书文件，将证书文件放在Nginx安装目录cert中，一般为`/etc/nginx`
4. 配置nginx，主要是将http重定向到https上
```
server {
    listen       80;
    server_name  _;

    location / {
        rewrite ^/(.*)$ https://yongxinxue.xin/$1 permanent;
    }
}

server {
    listen 443;
    server_name _;
    ssl on;
    ssl_certificate   cert/214462643660969.pem;
    ssl_certificate_key  cert/214462643660969.key;
    ssl_session_timeout 5m;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;
    location / {
        if ( $host != 'yongxinxue.xin' ){
            rewrite ^/(.*)$ https://yongxinxue.xin/$1 permanent;
        }
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```


