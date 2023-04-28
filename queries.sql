SELECT * FROM users;
SELECT * FROM vehicle;
SELECT * FROM vehicle_records;
SELECT * FROM gasoline;

UPDATE vehicle
SET year_made = 1994, make = "Mazda", model = "Miata"
WHERE id = 2;

SELECT * FROM vehicle
JOIN users ON users.id = user_id;

SELECT * FROM vehicle_records
WHERE user_id = 1;

DELETE FROM users
WHERE id = 3;

DELETE FROM vehicle_records
WHERE id > 1;
