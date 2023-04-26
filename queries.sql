SELECT * FROM users;
SELECT * FROM vehicle;
SELECT * FROM vehicle_records;
SELECT * FROM gasoline;

SELECT * FROM vehicle
JOIN users ON users.id = user_id;

DELETE FROM users
WHERE id >= 2;

DELETE FROM vehicle
WHERE id >= 2;
