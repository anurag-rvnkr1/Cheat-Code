/*
180. Consecutive Numbers

Table: Logs

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| num         | int  |
+-------------+------+
id is the primary key.
id is an auto-increment column.

Write a solution to find all numbers that appear at least three times consecutively.

Return the result table in any order.

Example:

Input:
Logs
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+

Output:
+-------------------+
| ConsecutiveNums   |
+-------------------+
| 1                 |
+-------------------+

Explanation:
Number 1 appears three times consecutively at ids 1, 2, and 3.
*/

-- Self Join

SELECT DISTINCT
    l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2
    ON l1.id + 1 = l2.id
JOIN Logs l3
    ON l2.id + 1 = l3.id
WHERE l1.num = l2.num
  AND l2.num = l3.num;
