/*
183. Customers Who Never Order

Table: Customers

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+

id is the primary key for this table.
Each row contains the customer's ID and name.

Table: Orders

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+

id is the primary key for this table.
customerId is a foreign key referencing Customers.id.

Write a solution to find all customers who never placed an order.

Return the result table in any order.

Example:

Input:
Customers
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+

Orders
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+

Output:
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+

Explanation:
Henry and Max do not have any orders in the Orders table.
*/

-- LEFT JOIN

SELECT
    c.name AS Customers
FROM Customers c
LEFT JOIN Orders o
    ON c.id = o.customerId
WHERE o.id IS NULL;
