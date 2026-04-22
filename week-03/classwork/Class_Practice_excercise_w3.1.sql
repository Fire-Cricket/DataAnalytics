USE northwind;

-- Question 1
-- Task: Write a query to list the CategoryID, CategoryName, and Description of every category in 
-- the Northwind database.
-- Hint: Look at the Categories table. Use SELECT to pick only the columns you need.

SELECT CategoryID, CategoryName, Description
FROM Categories;

-- Question 2
-- Task: Write a query to find all products where the quantity per unit contains the word 'box' 
-- (e.g., '12 boxes' or '24 - 12 oz boxes').
-- Hint: Use the LIKE operator with wildcard characters to search for partial text matches inside 
-- the QuantityPerUnit column of the Products table.

SELECT Productid, productname, QuantityPerUnit 
FROM Products 
WHERE QuantityPerUnit LIKE '%box%';

-- Question 3
-- Task: Write a query to list all products that are currently discontinued. Display the ProductID, 
-- ProductName, and Discontinued columns.
-- Hint: The Discontinued column in the Products table stores 1 for discontinued and 0 for active.

SELECT ProductId, ProductName, Discontinued
FROM Products
WHERE Discontinued = 0;

-- Question 4
-- Task: Write a query to display the full name of every employee by combining their first and last 
-- name into a single column. Label the combined column FullName.
-- Hint: Look at the Employees table. Use string concatenation (+ in SQL Server, || in 
-- SQLite/PostgreSQL) to combine FirstName and LastName with a space between them.

SELECT EmployeeID, CONCAT(FirstName, ' ', LastName) AS FullName
FROM Employees;

-- Question 5
-- Task: Write a query to list all customers located in either Germany or France. Display the 
-- CustomerID, CompanyName, and Country.
-- Hint: You can use IN to test against a list of values instead of writing multiple OR conditions.

SELECT CustomerID, CompanyName, Country
FROM Customers 
WHERE Country = 'Germany' OR Country = 'France';

-- Question 6
-- Task: How many total orders have been placed in the Orders table? Write a query that returns 
-- this count and labels it TotalOrders.
-- Hint: Use the COUNT() aggregate function on the primary key of the Orders table.

SELECT COUNT(OrderID) AS TotalOrders
FROM Orders;

-- Question 7
-- Task: Write a query to list all suppliers whose contact title is either 'Sales Representative' or 
-- 'Sales Manager'. Show SupplierID, CompanyName, ContactName, and ContactTitle.
-- Hint: Use the IN operator or two OR conditions in your WHERE clause against the Suppliers 
-- table.

SELECT SupplierID, CompanyName, ContactName, ContactTitle
FROM Supplier
WHERE ContactTitle IN ('Sales Representative', 'Sales Manager');

-- Question 8
-- Task: Write a query to find all orders that were shipped to the USA. Display OrderID, 
-- CustomerID, ShipCountry, and ShippedDate.
-- Hint: Filter the Orders table using the ShipCountry column.

SELECT OrderID, CustomerID, ShipCountry, ShippedDate
FROM Orders
WHERE ShipCountry = 'USA';

-- Question 9
-- Task: Examine the Orders table. It records a required date and an actual shipped date. Write a 
-- query to find all orders where the product was shipped after the required date (i.e., the 
-- shipment was late). Display OrderID, CustomerID, RequiredDate, and ShippedDate.
-- Hint: Compare two date columns using the > operator in a WHERE clause.

SELECT OrderID, CustomerID, RequiredDate, ShippedDate
FROM Orders
WHERE ShippedDate > RequiredDate;

-- Question 10
-- Task: Examine the Products table. It contains a column called UnitsInStock and a column called 
-- ReorderLevel. Write a query that identifies products that need to be reordered — that is, 
-- products where the current stock is at or below the reorder level and the product is NOT 
-- discontinued.
-- Hint: Combine two conditions in the WHERE clause using AND.

SELECT ProductID, ProductName, UnitsInStock, ReorderLevel, Discontinued
FROM Products
WHERE UnitsInStock <= ReorderLevel AND Discontinued = 0;


