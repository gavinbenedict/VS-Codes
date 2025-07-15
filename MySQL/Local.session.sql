CREATE DATABASE college;
USE college;

CREATE TABLE students(
	Sno INT PRIMARY KEY AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    age INT,
    roll VARCHAR(20) UNIQUE,
    department VARCHAR(100)
);

INSERT INTO students(name, age, roll, department)
VALUES
('Gavin',29,'24AD143','ADS'),
('Ashwath',18,'24AD826','ADS'),
('Shan',18,'24IT420','IT'),
('Asvanth',18,'24AD104','CSE');

SELECT * FROM students;

UPDATE students
SET Department='ADS'
WHERE name='Asvanth';

DELETE FROM students
WHERE name='Shan';

DROP TABLE students;

DROP DATABASE college;

SET SQL_SAFE_UPDATES = 0;


