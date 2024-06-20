UPDATE users SET salary = ROUND(RAND() * 10000, 2);

SELECT first_name, salary FROM users
WHERE salary BETWEEN 1000 AND 1500
ORDER BY salary ASC;