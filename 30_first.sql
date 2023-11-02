DROP DATABASE IF EXISTS school;

-- 注释
CREATE DATABASE school DEFAULT CHARSET utf8;

-- 切换到 school 数据库
USE school;

-- 什么叫二维表? 有行有列就是二维表, 一行就是一条记录, 一列就是一个字段!

-- 创建学生表(tb是一个命名习惯, 因为数据库中除了表, 还有视图, 触发器, 索引等等, 为了区分一下)
CREATE TABLE tb_student(
	stuid INT NOT NULL, -- 
	stuname VARCHAR(20) NOT NULL,
	sex BIT DEFAULT 1, 
	birth DATE, 
	PRIMARY KEY (stuid)
);

