
-- 1. Total Revenue
SELECT SUM(revenue) AS total_revenue
FROM retail_sales;

-- 2. Total Orders
SELECT COUNT(DISTINCT order_id) AS total_orders
FROM retail_sales;

-- 3. Total Units Sold
SELECT SUM(quantity) AS total_units_sold
FROM retail_sales;

-- 4. Product-wise Revenue
SELECT product, SUM(revenue) AS total_revenue
FROM retail_sales
GROUP BY product
ORDER BY total_revenue DESC;

-- 5. Region-wise Revenue
SELECT region, SUM(revenue) AS total_revenue
FROM retail_sales
GROUP BY region
ORDER BY total_revenue DESC;

-- 6. Monthly Revenue
SELECT strftime('%Y-%m', order_date) AS month,
       SUM(revenue) AS monthly_revenue
FROM retail_sales
GROUP BY month
ORDER BY month;

-- 7. Online vs Retail Sales
SELECT sales_channel, SUM(revenue) AS total_revenue
FROM retail_sales
GROUP BY sales_channel;
