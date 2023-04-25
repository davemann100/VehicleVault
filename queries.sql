SELECT * FROM users;
SELECT * FROM vehicle_records;
SELECT * FROM gasoline;

INSERT INTO users (first_name, last_name, email, password, make, model, spec)
VALUES ("Ricky", "Bobby", "Ricky@bobby.com", "password123", 0, 0, 0);

DELETE FROM users
WHERE id > 0;

