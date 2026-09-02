USE northwind;

SELECT * FROM customers WHERE City = 'London' OR City = 'Paris';

SELECT * FROM customers LIMIT 10;

SELECT * FROM customers WHERE City = 'London' AND ContactTitle = 'Sales Representative';

SELECT ProductName, UnitsInStock, UnitPrice FROM Products WHERE UnitsInStock > 0 AND UnitPrice >= 30;

SELECT * FROM products WHERE ProductName LIKE 'c%';	

SELECT * FROM customers WHERE City IN ("Paris", "London");

SELECT * FROM products WHERE UnitsInStock BETWEEN 0 AND 20;

SELECT CONCAT(FirstName, " ", LastName) AS "FullName", FirstName, LastName FROM employees;

SELECT * FROM customers WHERE Region IS NOT NULL;

-- + - * / % Arithmetic operators

SELECT ProductName, UnitsInStock * UnitPrice AS "TotalPrice" FROM products; 

SELECT MAX(UnitPrice) FROM products;

SELECT CategoryID, AVG(UnitPrice) FROM products GROUP BY CategoryID
