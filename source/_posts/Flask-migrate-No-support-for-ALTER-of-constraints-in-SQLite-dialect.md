---
title: Flask-migrate No support for ALTER of constraints in SQLite dialect
date: 2018-01-08 16:39:16
tags: flask
categories: flask网站总结
---

# 问题
由于sqlite不支持`DROP COLUMN`、`ALTER COLUMN`、`ADD CONSTRAINT`等操作，如果flask使用了sqlite做数据库，flask-migrate不能自动迁移

# 解决
两种途径，都来自[这里](https://github.com/miguelgrinberg/Flask-Migrate/issues/61)
## 方法1
换MySql或者Postgres，也是flask-migrate作者的建议。
## 方法2
在创建db的地方
```python
from sqlalchemy import MetaData

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
```
enabled batch mode for auto-generated migrations by adding a `render_as_batch=config.get_main_option('sqlalchemy.url').startswith('sqlite:')` argument to `context.configure()` in `run_migrations_online()` in `migrations/env.py`.
```python
def run_migrations_online():
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    engine = engine_from_config(
                config.get_section(config.config_ini_section),
                prefix='sqlalchemy.',
                poolclass=pool.NullPool)

    connection = engine.connect()
    context.configure(
                connection=connection,
                target_metadata=target_metadata,
                render_as_batch=config.get_main_option('sqlalchemy.url').startswith('sqlite:///')
                )

    try:
        with context.begin_transaction():
            context.run_migrations()
    finally:
        connection.close()
```
方法2试用到现在修改column和foreign-key没遇到什么问题，但是作者不推荐，用得很心虚（sadly）
