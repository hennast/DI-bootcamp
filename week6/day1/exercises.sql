create table items (
	id serial primary key,
	item varchar(20),
	price float
)
create table customers (
	id serial primary key,
	first_name varchar(20),
	last_name varchar(20)
)
insert into items (id, item, price)
values
(1, 'small desk', 100),
(2, 'large desk', 400),
(3, 'fan', 80)
insert into customers (id, first_name, Last_name)
values
(1, 'Greg', 'Jones'),
(2, 'Sandra','Jones'),
(3, 'Scott', 'Scott'),
(4, 'Trevor', 'Green'),
(5, 'Melanie' 'Johnson')
select * from items;
select * from items where (price > 80);
select * from customers where last_name = 'smith';
select * from customers where last_name = 'jones';
select * from customers where first_name <> 'Scott';




