/*
184. Department Highest Salary

Table: Employee

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+

id is the primary key for this table.
departmentId is a foreign key referencing Department.id.
Each row contains an employee's salary and department.

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+

id is the primary key for this table.
Each row contains the department name.

Write a solution to find employees who have the highest salary in each department.

Return the result table in any order.

Example:

Input:
Employee
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+

Department
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+

Output:
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| IT         | Max      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+

Explanation:
Jim and Max share the highest salary in the IT department.
Henry has the highest salary in the Sales department.
*/

-- JOIN + GROUP BY + MAX

SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
JOIN Department d
    ON e.departmentId = d.id
JOIN (
    SELECT
        departmentId,
        MAX(salary) AS maxSalary
    FROM Employee
    GROUP BY departmentId
) highest
    ON e.departmentId = highest.departmentId
   AND e.salary = highest.maxSalary;
