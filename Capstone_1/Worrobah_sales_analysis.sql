-- Jordan Worrobah Sales Analysis
-- Territory: See Ellefson

USE sample_sales;
USE  Sample_Sales;
SHOW TABLES;

SELECT * FROM inventory_categories;
SELECT * FROM inventory_subategories;
SELECT * FROM management;
SELECT * FROM online_sales;
SELECT * FROM products;
SELECT * FROM shipper_list;
SELECT * FROM store_locations;
SELECT * FROM store_sales;

SELECT 
    SUM(ss.Sale_Amount) AS total_revenue,
    MIN(ss.Transaction_Date) AS start_date,
    MAX(ss.Transaction_Date) AS end_date
FROM store_sales ss
JOIN store_locations sl 
    ON ss.Store_ID = sl.StoreId
JOIN management m 
    ON sl.State = m.State
WHERE m.SalesManager = 'See Ellefson';

SELECT 
    DATE_FORMAT(ss.Transaction_Date, '%Y-%m') AS Month,
    SUM(ss.Sale_Amount) AS 'Monthly Revenue'
FROM store_sales ss
JOIN store_locations sl 
    ON ss.Store_ID = sl.StoreId
JOIN management m
    ON sl.State = m.State
WHERE m.SalesManager = 'See Ellefson'
GROUP BY month
ORDER BY month;

SELECT m.Region,
	m.SalesManager,
    SUM(SS.Sales_Amount) AS total_revenue