USE northwind;

-- What is the product name(s) of the most expensive products?
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice = (SELECT MAX(UnitPrice)
FROM Products);

-- What is the product name(s) and categories of the least expensive products?
SELECT 
    p.ProductName,
    c.CategoryName,
    p.UnitPrice
FROM Products p
INNER JOIN Categories c
    ON p.CategoryID = c.CategoryID
WHERE p.UnitPrice = (
    SELECT MIN(UnitPrice)
    FROM Products
); 

-- What is the order id, shipping name and shipping address of all orders shipped via "Federal Shipping"?
SELECT 
    OrderID,
    ShipName,
    ShipAddress
FROM Orders
WHERE ShipVia = (
    SELECT ShipperID
    FROM Shippers
    WHERE CompanyName = 'Federal Shipping'
);

-- What are the order ids of the orders that included "Sasquatch Ale"?
SELECT DISTINCT o.OrderID
FROM Orders o
INNER JOIN `order details` od
    ON o.OrderID = od.OrderID
INNER JOIN Products p
    ON od.ProductID = p.ProductID
WHERE p.ProductName = 'Sasquatch Ale';

-- What is the name of the employee that sold order 10266?
SELECT 
    e.FirstName,
    e.LastName
FROM Orders o
INNER JOIN Employees e
    ON o.EmployeeID = e.EmployeeID
WHERE o.OrderID = 10266;

-- What is the name of the customer that bought order 10266?
SELECT c.CompanyName
FROM Orders o
INNER JOIN Customers c
    ON o.CustomerID = c.CustomerID
WHERE o.OrderID = 10266;