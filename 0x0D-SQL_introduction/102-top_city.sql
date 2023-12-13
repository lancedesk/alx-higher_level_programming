-- Calculate the average temperature (Fahrenheit) for each city during July and August, and display the top 3 cities
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
