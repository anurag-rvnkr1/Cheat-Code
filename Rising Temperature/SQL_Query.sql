/*
197. Rising Temperature

Table: Weather

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| recordDate  | date |
| temperature | int  |
+-------------+------+

id is the primary key for this table.
There are no duplicate recordDate values.
Each row contains the temperature on a specific date.

Write a solution to find all dates where the temperature was higher than the previous day.

Return the ids of those dates in any order.

Example:

Input:
Weather
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+

Output:
+----+
| id |
+----+
| 2  |
| 4  |
+----+

Explanation:
2015-01-02 has a higher temperature than 2015-01-01.
2015-01-04 has a higher temperature than 2015-01-03.
*/

-- Self Join + DATEDIFF

SELECT
    w1.id
FROM Weather w1
JOIN Weather w2
    ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;
