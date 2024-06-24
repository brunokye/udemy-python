SELECT u.first_name, p.bio FROM users u
JOIN profiles p ON u.id = p.user_id
WHERE u.first_name = 'Zia';

UPDATE users AS u 
JOIN profiles p ON u.id = p.user_id
SET p.bio = CONCAT(p.bio, ' atualizado')
WHERE u.first_name = 'Zia';