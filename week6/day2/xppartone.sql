-- All items, ordered by price (lowest to highest).
-- SELECT * FROM items ORDER BY price asc

-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
-- Select * from items WHERE price >= 80 ORDER BY price DESC 

-- The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
--  Select first_name, last_name from customers WHERE id <= 3 ORDER BY first_name ASC 

-- All last names (no other columns!), in reverse alphabetical order (Z-A)
-- select last_name FROM customers ORDER BY last_name DESC