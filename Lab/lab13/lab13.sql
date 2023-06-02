.read data.sql

CREATE TABLE bluedog AS
  -- SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
  SELECT color, pet FROM students WHERE pet = 'dog' AND color = 'blue';

CREATE TABLE bluedog_songs AS
  -- SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
  SELECT color, pet, song FROM students WHERE pet = 'dog' AND color = 'blue';

CREATE TABLE smallest_int_having AS
  -- SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
  SELECT time, smallest FROM students GROUP BY smallest HAVING COUNT(*) = 1;

CREATE TABLE matchmaker AS
  -- SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
  SELECT a.pet, a.song, a.color, b.color FROM students AS a, students AS b
    WHERE a.time < b.time AND a.pet = b.pet AND a.song = b.song;

CREATE TABLE sevens AS
  -- SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
  SELECT s.seven FROM students AS s, numbers AS c WHERE s.number = 7 AND c.'7' = 'True' AND s.time = c.time;


CREATE TABLE average_prices AS
  -- SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
  SELECT category, AVG(MSRP) AS average_price FROM products GROUP BY category;


CREATE TABLE lowest_prices AS
  -- SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
  SELECT store, item, MIN(price) AS lowest_price FROM inventory GROUP BY item;


CREATE TABLE shopping_list AS
  -- SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
  SELECT name, store FROM products as p, lowest_prices as l
    WHERE p.name = l.item 
    GROUP BY category HAVING MIN(MSRP/rating);


CREATE TABLE total_bandwidth AS
  -- SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
  SELECT SUM(s.Mbs) FROM stores AS s, shopping_list AS sl 
    WHERE s.store = sl.store;

