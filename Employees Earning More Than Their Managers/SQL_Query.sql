/*
181. Employees Earning More Than Their Managers

Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+

id is the primary key for this table.
Each row indicates the ID of an employee, their name, salary,
and the ID of their manager.

Write a solution to find the employees who earn more than their managers.

Return the result table in any order.

Example:

Input:
Employee
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+

Output:
+----------+
| Employee |
+----------+
| Joe      |
+----------+

Explanation:
Joe earns 70000 while his manager Sam earns 60000.
Therefore, Joe should be returned.
*/

-- Self Join

SELECT
    e1.name AS Employee
FROM Employee e1
JOIN Employee e2
    ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;
