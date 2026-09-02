USE northwind;

SELECT COUNT(employeeID) FROM employees WHERE City = 'London';   

SELECT count(ProductID) FROM products WHERE Discontinued = 1;

SELECT ProductName, ProductID FROM products WHERE UnitPrice < 5;

SELECT * FROM categories WHERE CategoryName LIKE 'b%' OR CategoryName LIKE 's%';

SELECT count(orderID) FROM orders WHERE EmployeeID = 5 OR EmployeeID = 7;

SELECT CONCAT(FirstName, ' ', LastName) AS FullName FROM employees;

SELECT DISTINCT Country FROM Customers WHERE Region IS NOT NULL; 

SELECT * FROM `order details`;

SELECT 
    OrderID,
    UnitPrice,
    Quantity,
    Discount,
    UnitPrice * Quantity AS 'Gross Total',
    UnitPrice * (1 - Discount) * Quantity AS 'Net Total'
FROM
    `order details`
ORDER BY `Net Total` DESC;
 
SELECT * FROM products; 
 
SELECT ProductName AS 'Single quote products' FROM products WHERE INSTR(ProductName, "'") > 0;
 
SELECT
    CONCAT(FirstName, ' ', LastName) AS FullName,
    TIMESTAMPDIFF(YEAR, BirthDate, SYSDATE()) AS Age,
    CASE
		WHEN TIMESTAMPDIFF(YEAR, BirthDate, SYSDATE()) > 65 THEN 'Retired'
        WHEN TIMESTAMPDIFF(YEAR, BirthDate, SYSDATE()) > 60 THEN 'Retirement due'
        ELSE 'More than 5 years to go'
	END AS 'Retirement Status'
FROM 
	Employees;
    
SELECT CategoryID, AVG(ReorderLevel) FROM Products GROUP BY CategoryID ORDER BY AVG(ReorderLevel) DESC;

-- ---------------------------------------------
-- JOIN QUESTIONS
-- ---------------------------------------------

SELECT 
    s.CompanyName, AVG(p.UnitsOnOrder)
FROM
    Products p
        INNER JOIN
    Suppliers s ON p.SupplierID = s.SupplierID
GROUP BY s.CompanyName;
    
    
SELECT 
    o.OrderID,
    c.CompanyName AS 'Company Name',
    CONCAT(e.FirstName, ' ', e.LastName) AS 'Employee Name',
    o.OrderDate,
    o.Freight
FROM
    Orders o
        INNER JOIN
    Customers c ON o.CustomerID = c.CustomerID
        INNER JOIN
    Employees e ON o.EmployeeID = e.EmployeeID;


SELECT * FROM products;

SELECT 
    *
FROM
    `Order Details`
WHERE
    ProductID IN (SELECT 
            ProductID
        FROM
            Products
        WHERE
            Discontinued = 1);



SELECT 
    OrderID, od.ProductID, od.UnitPrice, Quantity, Discount
FROM
    `Order Details` od
        INNER JOIN
    Products p ON od.ProductID = p.ProductID
WHERE
    p.Discontinued = 1;


