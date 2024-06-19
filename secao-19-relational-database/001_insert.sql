USE base_de_dados;
SHOW tables;
DESCRIBE users;

INSERT INTO users (first_name, last_name, email, password_hash) VALUES
("Helena", "A.", "1@email.com", "3_hash"),
("Joana", "B.", "2@email.com", "4_hash"),
("Rosana", "C.", "3@email.com", "5_hash");