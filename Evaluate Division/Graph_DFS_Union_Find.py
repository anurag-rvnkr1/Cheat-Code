'''
399. Evaluate Division

You are given equations representing division relationships between variables.

Each equation:
    Ai / Bi = values[i]

Return the answers to the given queries.

If a query cannot be determined, return -1.0.

Example 1:
    Input:
        equations = [["a","b"],["b","c"]]
        values = [2.0,3.0]
        queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

    Output:
        [6.0,0.5,-1.0,1.0,-1.0]

Example 2:
    Input:
        equations = [["a","b"],["b","c"],["bc","cd"]]
        values = [1.5,2.5,5.0]
        queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

    Output:
        [3.75,0.4,5.0,0.2]

Example 3:
    Input:
        equations = [["a","b"]]
        values = [0.5]
        queries = [["a","b"],["b","a"],["a","c"],["x","y"]]

    Output:
        [0.5,2.0,-1.0,-1.0]

Constraints:
    1 <= equations.length <= 20
    equations[i].length == 2
    values.length == equations.length
    0.0 < values[i] <= 20.0
    1 <= queries.length <= 20
'''

# Graph + DFS

from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:

        graph = defaultdict(list)

        # Build bidirectional weighted graph.
        for (numerator, denominator), value in zip(equations, values):
            graph[numerator].append((denominator, value))
            graph[denominator].append((numerator, 1 / value))

        def dfs(current, target, product, visited):
            if current == target:
                return product

            visited.add(current)

            for neighbor, weight in graph[current]:
                if neighbor not in visited:
                    answer = dfs(
                        neighbor,
                        target,
                        product * weight,
                        visited
                    )

                    if answer != -1.0:
                        return answer

            return -1.0

        answers = []

        for source, destination in queries:

            if source not in graph or destination not in graph:
                answers.append(-1.0)

            elif source == destination:
                answers.append(1.0)

            else:
                answers.append(
                    dfs(source, destination, 1.0, set())
                )

        return answers


# Example usage
solution = Solution()

# Example 1
equations1 = [["a","b"],["b","c"]]
values1 = [2.0,3.0]
queries1 = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

print(solution.calcEquation(equations1, values1, queries1))
# Output: [6.0,0.5,-1.0,1.0,-1.0]

# Example 2
equations2 = [["a","b"],["b","c"],["bc","cd"]]
values2 = [1.5,2.5,5.0]
queries2 = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

print(solution.calcEquation(equations2, values2, queries2))
# Output: [3.75,0.4,5.0,0.2]

# Example 3
equations3 = [["a","b"]]
values3 = [0.5]
queries3 = [["a","b"],["b","a"],["a","c"],["x","y"]]

print(solution.calcEquation(equations3, values3, queries3))
# Output: [0.5,2.0,-1.0,-1.0]

# Example 4
equations4 = [["x","y"],["y","z"]]
values4 = [4.0,0.5]
queries4 = [["x","z"],["z","x"],["y","x"]]

print(solution.calcEquation(equations4, values4, queries4))
# Output: [2.0,0.5,0.25]

# Example 5
equations5 = [["m","n"],["n","o"],["o","p"]]
values5 = [2.0,3.0,4.0]
queries5 = [["m","p"],["p","m"],["m","o"]]

print(solution.calcEquation(equations5, values5, queries5))
# Output: [24.0,1/24,6.0]

# Example 6
equations6 = [["a","b"],["c","d"]]
values6 = [2.0,5.0]
queries6 = [["a","d"],["c","d"],["b","a"]]

print(solution.calcEquation(equations6, values6, queries6))
# Output: [-1.0,5.0,0.5]
