-- Create the database
CREATE DATABASE ProductDB;

-- Use the newly created database
USE ProductDB;

-- Create the Products table
CREATE TABLE Products (
    ID INT PRIMARY KEY IDENTITY(1,1),
    Name VARCHAR(255) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL
);
Drop table Products;
