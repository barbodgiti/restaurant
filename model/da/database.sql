create database gks;

create table gks.user_tbl(
    id int primary key auto_increment,
    name varchar(20),
    family varchar(40),
    username varchar(30),
    password varchar(12),
    phone varchar(11)
);



