---
title: nginx 开启gzip
date: 2018-01-09 12:30:58
tags: nginx配置
categories: flask网站总结
---

## nginx配置
```
http {
    ...
    gzip on;
    
    gzip_min_length 1k;
    # 启用gzip压缩的最小文件，小于设置值的文件将不会压缩

    gzip_buffers 16 64k;

    gzip_http_version 1.1;

    gzip_comp_level 6;
    # gzip 压缩级别，1-10，数字越大压缩的越好，也越占用CPU时间
    
    gzip_types text/plain application/x-javascript text/css application/xml application/javascript application/json;
    # 进行压缩的文件类型。

    gzip_vary on;
    # 是否在http header中添加Vary: Accept-Encoding

    gzip_disable "MSIE [1-6]\.";
    # 禁用IE 6 gzip
    ...
}
```
## 效果拔群
百度统计的测试结果，从12s提高到6s

![](http://ot0uaqt93.bkt.clouddn.com/18-1-9/94641900.jpg "-6s, excited!") 
