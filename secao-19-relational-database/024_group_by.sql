SELECT first_name, COUNT(id) AS total FROM users
GROUP BY first_name ORDER BY total DESC;

SELECT u.first_name, COUNT(u.id) AS total FROM users AS u
JOIN profiles AS p ON u.id = p.user_id 
WHERE u.first_name = 'Hayfa'
GROUP BY u.first_name
ORDER BY total DESC;
