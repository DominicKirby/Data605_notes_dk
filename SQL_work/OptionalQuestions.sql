USE northwind;

-- 1
SELECT CONCAT(TitleOfCourtesy, " ", FirstName, " ", LastName) AS Name, City FROM employees;

-- 2
SELECT * FROM customers WHERE Country = "Germany";

-- 3
SELECT * FROM products WHERE UnitPrice > 25;

-- 4 
SELECT * FROM orders WHERE OrderDate LIKE "1997-07%";

-- 5
SELECT p.ProductName, c.CategoryName FROM products p INNER JOIN categories c ON c.CategoryID = p.CategoryID WHERE c.CategoryName = 'Beverages';

-- 6
SELECT * FROM customers WHERE City = "London"; 

-- 7
SELECT * FROM products WHERE UnitsInStock < 20;

-- 8 
SELECT * FROM suppliers WHERE Country = "USA";

-- 9
SELECT * FROM products WHERE Discontinued = 1;

-- 10
SELECT * FROM orders WHERE ShipCountry = "France";

-- 11
SELECT * FROM products ORDER BY UnitPrice DESC;

-- 12
SELECT * FROM customers ORDER BY CompanyName;

-- 13
SELECT * FROM employees ORDER BY HireDate;

-- 14
SELECT * FROM products ORDER BY UnitPrice DESC LIMIT 10;

-- 15
SELECT * FROM orders ORDER BY Freight DESC;

-- 16 
SELECT * FROM products ORDER BY CategoryID, ProductName;

-- 17
SELECT * FROM customers ORDER BY Country, City;

-- 18 
SELECT * FROM suppliers ORDER BY Country DESC, CompanyName;

-- 19
SELECT COUNT(productID) FROM products;

--

-- 29
SELECT country, COUNT(customerID) FROM customers GROUP BY country;

--

-- 39
SELECT country, COUNT(customerID) FROM customers WHERE  GROUP BY country;
