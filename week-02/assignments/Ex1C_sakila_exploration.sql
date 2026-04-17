/*
a) It shows columns, indexes, foreign keys, triggers. In columns it shows actor_id, first_name, last_name, and last_update,
b) In film it shows the same as under actor. 
Under columns it has film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating,
special_features, and last_update.alter
c) Film_actor has both actor_id and film_id
d) In rentals we see rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, and last_update. 
This information is pretty easy to read but mostly because I know what I am looking at. However, it is difficult to dechiper any useful information from it, 
such as, what has been rented the most, how often, what is often rented togther, etc. 
e) This is honestly even worse. THis is literally hundreds of records. This shows inventory_id, film_id, and store_id
f) To understand the names of all the films rented on an exact date I would need all three tables rental, inventory, and film. The rental tells when a rent happened and has the inventory_id
The inventory table has the film _idwhich connects it to the correct film. Finally the film table has the actual film name. 
*/
SELECT rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;

