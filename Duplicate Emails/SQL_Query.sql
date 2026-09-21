/*
182. Duplicate Emails

Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+

id is the primary key for this table.
Each row contains an email. Emails may appear more than once.

Write a solution to report all duplicate emails.

Return the result table in any order.

Example:

Input:
Person
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+

Output:
+---------+
| Email   |
+---------+
| a@b.com |
+---------+

Explanation:
The email "a@b.com" appears more than once, so it is returned.
*/

-- GROUP BY + HAVING

SELECT
    email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;
