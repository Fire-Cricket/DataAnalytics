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

SELECT OrderID,
CustomerID,
OrderDate
FROM Orders
WHERE OrderDate = '1997-01-01';

SELECT 
    OrderID,
    CustomerID,
    OrderDate
FROM Orders
WHERE YEAR(OrderDate) = 1997
  AND MONTH(OrderDate) = 6;
  
SELECT 
    ProductName,
    UnitPrice
FROM Products
ORDER BY ProductName DESC;

SELECT 
    CustomerID,
    City,
    Country,
    CompanyName
FROM Customers
ORDER BY Country ASC, CompanyName ASC;

SELECT 
    ProductName,
    UnitPrice
FROM Products
Order BY UnitPrice DESC
LIMIT 5;

SELECT 
    ProductName,
    UnitPrice
FROM Products
ORDER BY UnitPrice DESC
LIMIT 5, 5;

SELECT DISTINCT Country, City
FROM Customers
ORDER BY Country, City;

SELECT CONCAT(FirstName, ' ', LastName) AS 'Full Name',
Title
FROM Employees;

SELECT 
    ProductName, 
    UnitPrice AS 'Original Price', 
    UnitPrice * 0.9 AS 'Price With Discount'
FROM Products;

SELECT o.OrderID, c.CompanyName AS 'Customer', o.OrderDate
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
ORDER BY o.OrderDate DESC
LIMIT 5;

SELECT OrderID, CompanyName, OrderDate
FROM Orders 
JOIN Customers c USING (CustomerID)
ORDER BY OrderDate 
LIMIT 5;

SELECT p.ProductName,
       c.CategoryName,
       p.UnitPrice
FROM Products p
INNER JOIN Categories c ON p.CategoryID = c.CategoryID
ORDER BY c.CategoryName, p.ProductName
LIMIT 6;

SELECT ProductName,
       CategoryName,
       UnitPrice
FROM Products 
INNER JOIN Categories USING (CategoryID)
ORDER BY CategoryName, ProductName
LIMIT 6;

SELECT c.CompanyName, COUNT(o.OrderID) AS OrderCount
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CompanyName
ORDER BY OrderCount ASC
LIMIT 5;

