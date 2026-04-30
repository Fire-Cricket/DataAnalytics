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

-- What is total revenue overall for sales in the assigned territory, plus the start date and end date that tell you what period the data covers?
SELECT 
    SUM(ss.Sale_Amount) AS total_revenue,
    MIN(ss.Transaction_Date) AS start_date,
    MAX(ss.Transaction_Date) AS end_date
FROM store_sales ss
JOIN store_locations sl ON ss.Store_ID = sl.StoreId
JOIN management m ON sl.State = m.State
WHERE m.SalesManager = 'See Ellefson';

-- What is the month by month revenue breakdown for the sales territory?
SELECT 
    DATE_FORMAT(ss.Transaction_Date, '%Y-%m') AS Month,
    SUM(ss.Sale_Amount) AS 'Monthly Revenue'
FROM store_sales ss
JOIN store_locations sl ON ss.Store_ID = sl.StoreId
JOIN management m ON sl.State = m.State
WHERE m.SalesManager = 'See Ellefson'
GROUP BY month
ORDER BY month;

-- Provide a comparison of total revenue for the specific sales territory and the region it belongs to.
SELECT 
    m.Region,
    m.SalesManager,
    SUM(ss.Sale_Amount) AS 'Total Revenue'
FROM store_sales ss
JOIN store_locations sl ON ss.Store_ID = sl.StoreId
JOIN management m ON sl.State = m.State
WHERE m.Region = 'East'
GROUP BY m.Region, m.SalesManager
ORDER BY total_revenue DESC;

-- What is the number of transactions per month and average transaction size by product category for the sales territory?
SELECT 
    DATE_FORMAT(ss.Transaction_Date, '%Y-%m') AS month,
    ic.Category,
    COUNT(*) AS transactions,
    ROUND(AVG(ss.Sale_Amount), 2) AS 'Avg Transaction'
FROM store_sales ss
JOIN products p ON ss.Prod_Num = p.Prod_Num
JOIN inventory_subategories isc ON p.SubCategoryID = isc.SubCategoryID
JOIN inventory_categories ic ON isc.CategoryID = ic.CategoryID
JOIN store_locations sl ON ss.Store_ID = sl.StoreId
JOIN management m ON sl.State = m.State
WHERE m.SalesManager = 'See Ellefson'
GROUP BY month, ic.Category
ORDER BY month, ic.Category;

-- Can you provide a ranking of in-store sales performance by each store in the sales territory, 
-- or a ranking of online sales performance by state within an online sales territory?

SELECT 
    sl.StoreLocation,
    SUM(ss.Sale_Amount) AS Total_Revenue
FROM store_sales ss
JOIN store_locations sl ON ss.Store_ID = sl.StoreId
JOIN management m ON sl.State = m.State
WHERE m.SalesManager = 'See Ellefson'
GROUP BY sl.StoreLocation
ORDER BY Total_Revenue DESC;

-- What is your recommendation for where to focus sales attention in the next quarter?

-- My recommendation for this comapny is teh stores and categories that are bringing the most money should be priortized next quarter.
-- If they use most of their income to increase inventory and market stores that are performing the best they will defitly maximize their profit.
-- Also,  categories with higher average transaction values should receive more focus. For lower performing 
-- stores or categories targeted promotions may help increase their performance.
 