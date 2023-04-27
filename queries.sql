SELECT * FROM users;
SELECT * FROM vehicle;
SELECT * FROM vehicle_records;
SELECT * FROM gasoline;

SELECT * FROM vehicle
JOIN users ON users.id = user_id;

SELECT * FROM vehicle_records
WHERE user_id = 1;

DELETE FROM users
WHERE id >= 1;

DELETE FROM vehicle_records
WHERE id >= 2;
