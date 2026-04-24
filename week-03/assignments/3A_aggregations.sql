USE northwind;

-- Write a query to find the price of the cheapest item that Northwind sells.
-- Then write a second query to find the name of the product that has that price.

SELECT MIN(UnitPrice)
FROM Products;

SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice = (SELECT MIN(UnitPrice)
FROM Products);

-- Write a query to find the average price of all items that Northwind sells.
SELECT AVG(UnitPrice)
FROM Products;

SELECT AVG(UnitPrice)
FROM Products
WHERE UnitPrice = ROUND(UnitPrice);

-- Write a query to find the price of the most expensive item that Northwind sells. 
-- Then write a second query to find the name of the product with that price, plus the name of the supplier for that product.

SELECT MAX(UnitPrice)
FROM Products;

SELECT 
    p.ProductName,
    p.UnitPrice,
    s.CompanyName 
FROM Products p
INNER JOIN Suppliers s
    ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice = (
    SELECT MAX(UnitPrice)
    FROM Products
);

-- Write a query to find total monthly payroll (the sum of all the employees’ monthly salaries).
SELECT SUM(Salary)
FROM Employees;

-- Write a query to identify the highest salary and the lowest salary amounts which 
-- any employee makes. (Just the amounts, not the specific employees!)
SELECT MAX(Salary) AS Highest_Salary, MIN(Salary) AS Lowest_Salary
FROM Employees;

-- Write a query to find the name and supplier ID of each 
-- supplier and the number of items they supply. Hint: Join is your friend here.

SELECT s.CompanyName AS 'Supplier Name' , p.SupplierID, COUNT(p.ProductID) as 'Items Supplied'
FROM Products p
INNER JOIN Suppliers s
    ON p.SupplierID = s.SupplierID
GROUP BY s.SupplierID, s.CompanyName;

-- Write a query to find the list of all category names and the average price for items in each category.

SELECT 
    c.CategoryName,
    AVG(p.UnitPrice) 
FROM Products p
INNER JOIN Categories c
    ON p.CategoryID = c.CategoryID
GROUP BY c.CategoryName;

-- Write a query to find, for all suppliers that provide at 
-- least 5 items to Northwind, what is the name of each supplier and the number of items they supply.

SELECT 
    s.CompanyName,
    COUNT(p.ProductID) AS Items_Supplied
FROM Products p
INNER JOIN Suppliers s
    ON p.SupplierID = s.SupplierID
GROUP BY s.SupplierID, s.CompanyName
HAVING COUNT(p.ProductID) >= 5;

-- Write a query to list products currently in inventory by the product id, product name, 
-- and inventory value (calculated by multiplying unit price by the number of units on hand). 
-- Sort the results in descending order by value. If two or more have the same value, 
-- order by product name. If a product is not in stock, leave it off the list.

SELECT 
    ProductID,
    ProductName,
    UnitPrice * UnitsInStock AS InventoryValue
FROM Products
WHERE UnitsInStock > 0
ORDER BY InventoryValue DESC, ProductName ASC;