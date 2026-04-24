USE northwind;

-- Create a single query to list the product id, product name, 
-- unit price and category name of all products. Order by category name and within that, by product name.

SELECT 
    ProductID,
    ProductName,
    UnitPrice,
    CategoryName
FROM Products
JOIN Categories USING (CategoryID)
ORDER BY CategoryName ASC, ProductName ASC;

-- Create a single query to list the product id, product name, 
-- unit price and supplier name of all products that cost more than $75. 
--  by product name.

SELECT
	p.ProductID,
    p.ProductName,
    p.UnitPrice,
	s.CompanyName
FROM Products p
INNER JOIN Suppliers s ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice > 75
ORDER BY ProductName;

-- Create a single query to list the product id, product name, unit price, 
-- category name, and supplier name of every product. Order by product name.

SELECT 
    p.ProductID,
    p.ProductName,
    p.UnitPrice,
    c.CategoryName,
    s.CompanyName
FROM Products p
JOIN Categories c USING (CategoryID)
JOIN Suppliers s USING (SupplierID)
ORDER BY p.ProductName;
    
-- Create a single query to list the order id, ship name, 
-- ship address, and shipping company name of every order that 
-- shipped to Germany. Assign the shipping company name the alias 
-- ‘Shipper.’ Order by the name of the shipper, then the name of who it shipped to.

SELECT 
    o.OrderID,
    o.ShipName,
    o.ShipAddress,
    s.CompanyName AS Shipper
FROM Orders o
JOIN Shippers s 
    ON o.ShipVia = s.ShipperID
WHERE o.ShipCountry = 'Germany'
ORDER BY Shipper, o.ShipName;

-- Start from the same query as above (#4), 
-- but omit OrderID and add logic to group by ship name, 
-- with a count of how many orders were shipped for that ship name.

SELECT 
    o.ShipName,
    s.CompanyName AS Shipper,
    COUNT(*) AS OrderCount
FROM Orders o
JOIN Shippers s 
    ON o.ShipVia = s.ShipperID
WHERE o.ShipCountry = 'Germany'
GROUP BY o.ShipName, s.CompanyName
ORDER BY Shipper, o.ShipName;

-- Create a single query to list the order id, order date, 
-- ship name, ship address of all orders that included Sasquatch Ale.

SELECT DISTINCT
    o.OrderID,
    o.OrderDate,
    o.ShipName,
    o.ShipAddress
FROM `order details` od
JOIN orders o
    ON o.OrderID = od.OrderID
JOIN products p
    ON od.ProductID = p.ProductID
WHERE p.ProductName = 'Sasquatch Ale';