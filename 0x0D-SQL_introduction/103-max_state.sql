-- displays the max temperature of each state (ordered by State name).
SELECT city, max(value) AS max_temp
FROM temperatures
GROUP BY city
ORDER BY city DESC;
