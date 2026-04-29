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

SELECT 
    m.Region,
    m.SalesManager,
    SUM(ss.Sale_Amount) AS 'Total Revenue'
FROM store_sales ss
JOIN store_locations sl 
    ON ss.Store_ID = sl.StoreId
JOIN management m 
    ON sl.State = m.State
WHERE m.Region = 'East'
GROUP BY m.Region, m.SalesManager
ORDER BY total_revenue DESC;

SELECT 
    DATE_FORMAT(ss.Transaction_Date, '%Y-%m') AS month,
    ic.Category,
    COUNT(*) AS transactions,
    ROUND(AVG(ss.Sale_Amount), 2) AS 'Avg Transaction'
FROM store_sales ss
JOIN products p 
    ON ss.Prod_Num = p.Prod_Num
JOIN inventory_subategories isc 
    ON p.SubCategoryID = isc.SubCategoryID
JOIN inventory_categories ic 
    ON isc.CategoryID = ic.CategoryID
JOIN store_locations sl 
    ON ss.Store_ID = sl.StoreId
JOIN management m 
    ON sl.State = m.State
WHERE m.SalesManager = 'See Ellefson'
GROUP BY month, ic.Category
ORDER BY month, ic.Category;

SELECT 
    sl.StoreLocation,
    SUM(ss.Sale_Amount) AS 'Total Revenue'
FROM store_sales ss
JOIN store_locations sl 
    ON ss.Store_ID = sl.StoreId
JOIN management m 
    ON sl.State = m.State
WHERE m.SalesManager = 'See Ellefson'
GROUP BY sl.StoreLocation
ORDER BY 'Total Revenue' DESC;

-- My recommendation for this comapny is teh stores and categories that are bringing the most money should be priortized next quarter.
-- If they use most of their income to increase inventory and market stores that are performing the best they will defitly maximize their profit.
-- Also,  categories with higher average transaction values should receive more focus. For lower performing 
-- stores or categories targeted promotions may help increase their performance.
 