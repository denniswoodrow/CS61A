.read data.sql


CREATE TABLE average_prices AS
  SELECT category, AVG(MSRP) AS average_price 
  FROM products 
  GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, price 
  FROM inventory
  GROUP BY item
  HAVING MIN(price);


CREATE TABLE best_deal AS
  SELECT category, name, ROUND(MSRP / rating, 2) AS best_price
  FROM products
  GROUP BY category
  HAVING MIN(MSRP / rating);


CREATE TABLE shopping_list AS
  SELECT b.name AS name, i.store AS store
  FROM best_deal AS b, inventory AS i
  WHERE b.name = i.item
  GROUP BY b.category
  HAVING MIN(i.price);


CREATE TABLE total_bandwidth AS
  SELECT SUM(Mbs) AS bandwidth
  FROM stores AS s, shopping_list AS sl
  WHERE s.store = sl.store;


