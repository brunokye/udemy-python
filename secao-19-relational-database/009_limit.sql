SELECT id, first_name, email
FROM users WHERE id between 50 and 80
ORDER BY id ASC LIMIT 9 OFFSET 3;

SELECT id, first_name, email
FROM users WHERE id between 50 and 80
ORDER BY id ASC LIMIT 3, 9;