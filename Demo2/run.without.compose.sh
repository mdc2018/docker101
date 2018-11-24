#!/bin/bash

docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123123 -d mysql:5.7
docker exec -it mysql mysql -uroot -p123123 -e "create database test"
docker exec -it mysql mysql -uroot -p123123  test -e "create table Person (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,name VARCHAR(30) NOT NULL,age INT(4) NOT NULL)";
