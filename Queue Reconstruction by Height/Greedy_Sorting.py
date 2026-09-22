'''
406. Queue Reconstruction by Height

You are given an array people where:

    people[i] = [hi, ki]

    hi -> Height of the ith person.
    ki -> Number of people in front of this person who have a height
          greater than or equal to hi.

Return the queue reconstructed according to these properties.

Example 1:
    Input:
        people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

    Output:
        [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

Example 2:
    Input:
        people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]

    Output:
        [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

Constraints:
    1 <= people.length <= 2000
    people[i].length == 2
    0 <= hi <= 10^6
    0 <= ki < people.length
'''

# Greedy + Sorting

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort by height descending, then k ascending.
        people.sort(key=lambda person: (-person[0], person[1]))

        queue = []

        for person in people:
            queue.insert(person[1], person)

        return queue


# Example usage
solution = Solution()

# Example 1
people1 = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(solution.reconstructQueue(people1))
# Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

# Example 2
people2 = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
print(solution.reconstructQueue(people2))
# Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

# Example 3
people3 = [[5,0]]
print(solution.reconstructQueue(people3))
# Output: [[5,0]]

# Example 4
people4 = [[9,0],[7,0],[8,1],[6,2]]
print(solution.reconstructQueue(people4))
# Output: [[7,0],[9,0],[6,2],[8,1]]

# Example 5
people5 = [[5,0],[5,1],[5,2],[5,3]]
print(solution.reconstructQueue(people5))
# Output: [[5,0],[5,1],[5,2],[5,3]]

# Example 6
people6 = [[8,0],[4,2],[4,1],[5,0],[6,1]]
print(solution.reconstructQueue(people6))
# Output: [[5,0],[6,1],[4,1],[8,0],[4,2]]
