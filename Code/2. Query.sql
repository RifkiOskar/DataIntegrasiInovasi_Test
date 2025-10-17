-- Top Product --
SELECT TOP 5 
    product_name, 
    SUM(total_price) AS total_pendapatan
FROM analytic
GROUP BY product_name
ORDER BY total_pendapatan DESC;

-- Top Pelanggan --
SELECT TOP 10
    customer_id, 
    customer_location, 
    SUM(total_price) AS total_spent
FROM analytic
GROUP BY customer_id, customer_location
ORDER BY total_spent DESC

-- Trend Penjualan --
SELECT
    month,
    SUM(total_price) AS total_pendapatan
FROM analytic
GROUP BY month
ORDER BY month;