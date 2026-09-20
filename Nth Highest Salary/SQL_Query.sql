/*
177. Nth Highest Salary

Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key.

Write a solution to find the nth highest distinct salary from the Employee table.
If there is no nth highest salary, return NULL.

Example 1:

Input:
Employee
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

n = 2

Output:
+-------------------+
| getNthHighestSalary(2) |
+-------------------+
| 200               |
+-------------------+

Example 2:

Input:
Employee
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+

n = 2

Output:
+-------------------+
| getNthHighestSalary(2) |
+-------------------+
| NULL              |
+-------------------+
*/

-- MySQL Function + DISTINCT + ORDER BY + LIMIT

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;

    RETURN (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET N
    );
END;
