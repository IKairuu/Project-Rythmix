CREATE DATABASE music_manager;

USE music_manager; 

CREATE TABLE users (
	id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    user_password VARCHAR(50)
) ;
CREATE TABLE favorites (
	music_id INT,
	title VARCHAR(100),
    artist VARCHAR(100),
    duration TIME,
    file_name VARCHAR(100),
    user_id INT
);

CREATE TABLE playlist (
	id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) UNIQUE,
    artist VARCHAR(100),
    duration TIME,
    file_name VARCHAR(100),
    user_id int
) ;

SELECT* FROM playlist ;
SELECT * FROM users ;
SELECT * FROM favorites ;