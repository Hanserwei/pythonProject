# SQL语言大小写敏感
# SQL语句以;结尾
# SQL支持注释，-- 注释内容（--后面有一个空格）
# 单行注释也可以用# 直接注释掉
# 多行注释用/*注释内容*/

# DDL-库管理
# 查看数据库
# SHOW DATABASES；
# 使用数据库
# USE 数据库名称；
# 删除数据库
# DROP DATABASE 数据库名称；
# 查看当前使用的数据库
# SELECT DATABASE();
# 创建数据库
# CREATE　DATABASE 数据库名称 [CHARSET UTF8]；

# DDL-表操作
# SHOW TABLES；查看有哪些表，首先选择用哪个库
# DROP TABLE 表名称；
# DROP TABLE IF EXISTS;删除表
# 创建表
# CREATE　TABLE 表名称　(
#   列名称　列类型，
#   列名称　列类型，
#   .........
# )

# 常见的类型有int， float， varchar(长度)文本， date(日期)，　timestamp(时间戳类型)