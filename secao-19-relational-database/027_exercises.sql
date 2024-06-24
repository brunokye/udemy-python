-- 1) Insira 5 usuários
INSERT INTO users (first_name, last_name, email, password_hash) VALUES
('Maria', 'Miranda', 'email@a.com', round(rand() * 100000)),
('João', 'Ferreira', 'email@b.com', round(rand() * 100000)),
('Pedro', 'Garcia', 'email@c.com', round(rand() * 100000)),
('Rafael', 'Pereira', 'email@d.com', round(rand() * 100000)),
('Regina', 'Cristina', 'email@e.com', round(rand() * 100000));

UPDATE users SET salary = round(rand() * 10000, 2) WHERE id IN (114, 113, 112, 111, 110);

-- 2) Insira 5 perfís para os usuários inseridos
INSERT INTO profiles (bio, description, user_id) VALUES
('Bio Teste', 'Descrição Teste', 110),
('Bio Teste', 'Descrição Teste', 111),
('Bio Teste', 'Descrição Teste', 112),
('Bio Teste', 'Descrição Teste', 113),
('Bio Teste', 'Descrição Teste', 114);

-- 3) Insira permissões (roles) para os usuários inseridos
INSERT INTO users_roles (user_id, role_id) VALUES
(110, 3), (110, 4),
(111, 3), (111, 4),
(112, 3), (112, 4),
(113, 3), (113, 4),
(114, 3), (114, 4);


-- 4) Selecione os últimos 5 usuários por ordem decrescente
SELECT * FROM users ORDER BY id DESC LIMIT 5;

-- 5) Atualize o último usuário inserido
UPDATE users SET first_name = 'Joana' WHERE id = 114 ;

-- 6) Remova uma permissão de algum usuário
DELETE FROM users_roles WHERE user_id = 114 LIMIT 1;

-- 7) Remova um usuário que tem a permissão "PUT"
DELETE u FROM users AS u
INNER JOIN users_roles AS ur ON u.id = ur.user_id
INNER JOIN roles AS r ON ur.role_id = r.id
WHERE r.name = 'PUT' AND u.id = 19;

-- 8) Selecione usuários com perfís e permissões (obrigatório)
SELECT u.id AS user_id, u.first_name, r.name AS role, p.bio FROM users AS u
INNER JOIN profiles AS p ON u.id = p.user_id
INNER JOIN users_roles AS ur ON u.id = ur.user_id
INNER JOIN roles AS r ON ur.role_id = r.id;


-- 9) Selecione usuários com perfís e permissões (opcional)
SELECT u.id AS user_id, u.first_name, r.name AS role, p.bio FROM users AS u
LEFT JOIN profiles AS p ON u.id = p.user_id
LEFT JOIN users_roles AS ur ON u.id = ur.user_id
LEFT JOIN roles AS r ON ur.role_id = r.id;

-- 10) Selecione usuários com perfís e permissões ordenando por salário
SELECT u.id AS user_id, u.first_name, u.salary, r.name AS role, p.bio FROM users AS u
INNER JOIN profiles AS p ON u.id = p.user_id
INNER JOIN users_roles AS ur ON u.id = ur.user_id
INNER JOIN roles AS r ON ur.role_id = r.id
ORDER BY u.salary;
