-- a) The table that holds the items Northwind sells is called Products.
-- b) The table that holds the types/categories of the items Northwind sells is called Categories.
SELECT * FROM employees;
-- a) Her name is Margaret Peacock
SELECT * FROM Products;
-- a) 77 Records come back. You can limit how many rows come back in the task bar at the top of the query window.
SELECT * FROM categories;
-- a) The ID is 8. 
SELECT OrderID, OrderDate, ShipName, ShipCountry FROM Orders LIMIT 50;
