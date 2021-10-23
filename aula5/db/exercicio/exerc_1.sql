create database loja;

use loja;

create table produtos(
id int not null primary key auto_increment,
nome varchar(100) not null,
preco decimal(5,2),
id_categoria int
);

create table categoria(
id int not null primary key auto_increment,
nome varchar(100) not null
);


insert into produtos values (0, "Guarana", 10.5, 1);
insert into produtos values (0, "Pepsi", 11.5, 1);
insert into produtos values (0, "Fanta", 12.5, 1);
insert into produtos values (0, "Laranjinha", 13.5, 1);
insert into produtos values (0, "Coca", 14.5, 1);

INSERT  into categoria values (0, "Refrigerante");
INSERT  into categoria values (0, "Comida");

UPDATE produtos set nome = "Arroz", id_categoria = 2 WHERE id = 3;
UPDATE produtos set nome = "Feijao", id_categoria = 2 WHERE id = 4;

SELECT p.id , p.nome, p.preco, c.nome as categoria from produtos p 
join categoria c on p.id_categoria = c.id;