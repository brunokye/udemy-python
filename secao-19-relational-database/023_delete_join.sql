SELECT u.first_name, p.bio FROM users AS u
LEFT JOIN profiles p ON u.id = p.user_id
WHERE u.first_name = 'Zia';

DELETE p, u FROM users AS u
LEFT JOIN profiles AS p 
ON u.id = p.user_id
WHERE u.first_name = 'Zia';