-- SELECT * FROM customer
-- SELECT (first_name, last_name) AS full_name FROM customer 
-- SELECT DISTINCT create_date FROM customer

-- Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.
-- SELECT first_name, last_name, email from customer ORDER BY first_name desc

-- Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
-- SELECT * FROM film
-- select film_id, description, release_year, rental_rate FROM film ORDER BY rental_rate asc

-- Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.
-- SELECT * from address
-- SELECT address, phone from address WHERE district IN ('texas')

-- write a query to retrieve all movie details where the movie id is either 15 or 150.
-- SELECT * FROM film WHERE film_id in (15, 150)

-- Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.
-- SELECT film_id, title, description, length, rental_rate  FROM film WHERE title IN ('jaws')

-- No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.
-- SELECT film_id, title, description, length, rental_rate  FROM film WHERE title LIKE 'ja%'


-- Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
-- Bonus: Try to not use LIMIT.

-- SELECT * FROM film ORDER BY rental_rate limit 10
-- SELECT * FROM film ORDER BY rental_rate offset 10 limit 10

-- Write a query which will join the data in the customer table and the payment table. You want to get the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).



-- Select c.customer_id, c.first_name ||' '|| c.last_name as full_name, p.payment_date, p.amount
-- from payment as p
-- inner join customer as c
-- on p.customer_id = c.customer_id

-- You need to check your inventory. Write a query to get all the movies which are not in inventory.
-- select f.film_id, f.title from film as f where f.film_id not in (select film_id from inventory)

-- Write a query to find which city is in which country.
-- select city, country from city inner join country on city.country_id = country.country_id
 
--  Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dv
-- select c.first_name ||' '|| c.last_name as customer_name, s.first_name as staff_name
-- from customer as c
-- inner join staff as s
-- on c.store_id = s.store_id

