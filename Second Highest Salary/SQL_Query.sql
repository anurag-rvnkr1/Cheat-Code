/*
176. Second Highest Salary

Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key.

Write a solution to find the second highest distinct salary from the Employee table.
If there is no second highest salary, return NULL.

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

Output:
+----------------------+
| SecondHighestSalary  |
+----------------------+
| 200                  |
+----------------------+

Example 2:

Input:
Employee
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+

Output:
+----------------------+
| SecondHighestSalary  |
+----------------------+
| NULL                 |
+----------------------+
*/

-- DISTINCT + ORDER BY + LIMIT

SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
