-- la base de datos
CREATE DATABASE videogames_db;

-- Usar la base 
USE videogames_db;

-- Crear tabla de juegos
CREATE TABLE games (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    release_date DATE,
    genre VARCHAR(50)
);


CREATE TABLE developers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(50)
);


CREATE TABLE platforms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);


CREATE TABLE characters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    game_id INT,
    abilities TEXT,
    FOREIGN KEY (game_id) REFERENCES games(id)
);

-- tabla de puntuaciones
CREATE TABLE scores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT,
    user VARCHAR(100),
    score INT,
    date DATE,
    FOREIGN KEY (game_id) REFERENCES games(id)
);
