-- Jordan Worrobah
-- 4/20/2026
SHOW databases;

USE northwind;
SHOW TABLES;

SHOW TABLES;
SELECT ProductName, UnitPrice
FROM products;

SELECT * FROM Products;
SELECT 
    ProductName AS 'Product',
    UnitPrice AS 'Price(USD)',
    UnitsInStock AS 'Stock'
FROM Products;

SELECT CompanyName, 
	City, 
	Country 
FROM Customers 
WHERE Country = 'Germany';

SELECT 
	OrderID,
    CustomerID,
    ShipCountry,
    Freight
FROM Orders
WHERE ShipCountry = 'France';



SELECT ProductName, UnitPrice 
FROM Products 
WHERE UnitPrice > 50;

SELECT ProductName, 
	UnitsInStock, 
	ReorderLevel
FROM Products
WHERE UnitsInStock < ReorderLevel;

SELECT OrderID, Freight
FROM Orders
WHERE Freight >= 100;

SELECT ProductName,
	UnitPrice,
    UnitsInStock
FROM Products
WHERE UnitPrice > 20 AND UnitsInStock > 50;

SELECT  CompanyName, 
	Country
FROM Customers
WHERE Country = 'UK' OR Country = 'Ireland';

SELECT 
    ProductName,
    CategoryID,
    UnitPrice
FROM Products
WHERE CategoryID IN (1, 2)
AND UnitPrice < 20;
  
SELECT CompanyName, Country
FROM Customers
WHERE Country <> 'USA';

SELECT ProductName, Discontinued
FROM Products
WHERE NOT Discontinued;

SELECT 
    CompanyName,
    Country
FROM Customers
WHERE Country IN ('France', 'Germany', 'Spain');

SELECT ProductName, SupplierID
FROM Products
WHERE SupplierID NOT IN (1, 2, 3);

SELECT ProductName, UnitPrice
FROM Products
Where UnitPrice BETWEEN 10 AND 20;

SELECT OrderID, CustomerID, ShipRegion
FROM Orders
WHERE ShipRegion IS NULL;

SELECT FirstName, LastName, Region
FROM Employees
WHERE Region IS NOT NULL;

SELECT CompanyName
FROM Customers
WHERE CompanyName LIKE 'A%';
