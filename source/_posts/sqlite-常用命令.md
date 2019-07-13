---
title: sqlite 常用命令
typora-root-url: ../../source
date: 2018-01-22 23:49:20
tags: sqlite
categories: flask网站总结
---

### dump database
```
sqlite3 <database_file>
.output <dump_text_file>
.dump
.exit
```
### dump table
```
.output <dump_text_file>
.dump <table_name>
.exit
```
### dump table structure
```
.output <dump_text_file>
.schema
.exit
```
### dump data of a table into a text
```
.mode insert
.output <dump_text_file>
.dump <table_name>
.exit
```
```
.read <dump_text_file>
```
