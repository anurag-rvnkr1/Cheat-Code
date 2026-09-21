/*
196. Delete Duplicate Emails

Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+

id is the primary key (auto-increment).
Each row contains an email.
Duplicate emails may exist.

Write a solution to delete all duplicate emails, keeping only the row with the smallest id for each email.

After running your query, each email should appear exactly once.

Example:

Input:
Person
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+

Output:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+

Explanation:
The duplicate email "john@example.com" appears twice.
Keep the smallest id (1) and delete the other row.
*/

-- Self Join + DELETE

DELETE p1
FROM Person p1
JOIN Person p2
    ON p1.email = p2.email
WHERE p1.id > p2.id;
