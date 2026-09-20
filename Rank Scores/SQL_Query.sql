/*
178. Rank Scores

Table: Scores

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| score       | decimal |
+-------------+---------+
id is the primary key.
Each row contains the score of a game.

Write a solution to find the rank of each score.

The ranking should follow these rules:
    - The highest score gets rank 1.
    - Tied scores receive the same rank.
    - The next rank should be the next consecutive integer.
      (Dense Ranking)

Return the result table ordered by score in descending order.

Example:

Input:
Scores
+----+-------+
| id | score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+

Output:
+-------+------+
| score | rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
*/

-- DENSE_RANK()

SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores
ORDER BY score DESC;
