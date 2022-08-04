-- Get a list of all film languages.
-- select name from language

-- get a list of all films joined with their languages – select the following details : film title, description, and language name. Try your query with different joins:
-- Get all films, even if they don’t have languages.
-- Get all languages, even if there are no films in those languages.

-- select f.title, f.description, l.name from film as f
-- inner join language as l
-- on f.language_id = l.language_id

-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.
-- create table new_film (
-- id serial,
-- name varchar(100))

-- insert into new_film (name)
-- values
-- ('jaws'),
-- ('avengers:age of ultron')

-- reate a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, it’s review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.

-- create table customer_review(
-- review_id serial PRIMARY KEY,
-- fk_film_id int,
-- fk_language_id integer,
-- title varchar(75),
-- score int,
-- review_text varchar,    
-- last_update date,
-- foreign key (fk_film_id) references film (film_id) on delete cascade,    
-- foreign key (fk_language_id) references language (language_id)
-- )
-- linked it to the film table bc I think I mad a mistake creating the new_film table and wanted to check
-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.

-- select title from film
-- dd 2 movie reviews. Make sure you link them to valid objects in the other tables.
-- insert into customer_review(fk_film_id, title, score, review_text)
-- values
-- (279, 'elf murder', 7, 'bad movie')

-- Delete a film that has a review from the new_film table, what happens to the customer_review table?
-- delete from film where film_id = 279

