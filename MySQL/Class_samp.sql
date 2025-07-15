CREATE DATABASE shop;
USE shop;

CREATE TABLE customer(
	Sno INT PRIMARY KEY AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    age INT,
    roll VARCHAR(20) UNIQUE,
    department VARCHAR(100)
);

INSERT INTO customer(name, age, roll, department)
VALUES
('Gavin',29,'24AD143','ADS'),
('Ashwath',18,'24AD826','ADS'),
('Shan',18,'24IT420','IT'),
('Asvanth',18,'24AD104','CSE');

SELECT * FROM customers;
WHERE id

UPDATE customer
SET Department='ADS'
WHERE name='Asvanth';

DELETE FROM customer
WHERE name='Shan';

DROP TABLE customer;

DROP DATABASE college;

SET SQL_SAFE_UPDATES = 0;


