/*
175. Combine Two Tables

Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |
+-------------+---------+
personId is the primary key.

Table: Address

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |
+-------------+---------+
addressId is the primary key.

Write a solution to report the first name, last name, city, and state of each person.
If the address of a person is not present, report NULL instead.

Example:

Input:
Person:
+----------+----------+-----------+
| personId | lastName | firstName |
+----------+----------+-----------+
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |
+----------+----------+-----------+

Address:
+-----------+----------+----------+------------+
| addressId | personId | city     | state      |
+-----------+----------+----------+------------+
| 1         | 2        | New York | New York   |
| 2         | 3        | Leetcode | California |
+-----------+----------+----------+------------+

Output:
+-----------+----------+----------+----------+
| firstName | lastName | city     | state    |
+-----------+----------+----------+----------+
| Allen     | Wang     | NULL     | NULL     |
| Bob       | Alice    | New York | New York |
+-----------+----------+----------+----------+
*/

-- LEFT JOIN

SELECT
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a
ON p.personId = a.personId;
