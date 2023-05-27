SELECT store_id, AVG(CASE WHEN active = 1 THEN 1 ELSE 0 END) AS avg_active_customers
FROM customer
GROUP BY store_id;

-- Mağazalara göre ortalama aktif müşteri sayısı