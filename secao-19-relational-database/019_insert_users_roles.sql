INSERT INTO users_roles VALUES (23, 4);

INSERT INTO users_roles SELECT id AS user_id,
(SELECT id FROM roles ORDER BY RAND() LIMIT 1) AS role_id
FROM users;