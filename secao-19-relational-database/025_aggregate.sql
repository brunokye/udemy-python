SELECT 
MAX(salary) as max_salary,
MIN(salary) as min_salary,
ROUND(AVG(salary), 2) AS avg_salary,
SUM(salary) as sum_salary,
count(salary) as count_salary
FROM users;

SELECT 
u.first_name,
MAX(u.salary) as max_salary,
MIN(u.salary) as min_salary,
AVG(u.salary) as avg_salary,
SUM(u.salary) as sum_salary,
COUNT(u.id) as total
FROM users u
LEFT JOIN profiles AS p
ON u.id = p.user_id 
GROUP BY u.first_name
ORDER BY total DESC
LIMIT 5;