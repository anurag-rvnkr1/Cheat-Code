'''
293. Flip Game

You are playing a Flip Game with the following rules:

    - You are given a string currentState consisting of '+' and '-'.
    - Two consecutive "++" can be flipped into "--".
    - Return all possible states after one valid move.

Return the answer in any order.

Example 1:
    Input: currentState = "++++"
    Output: ["--++","+--+","++--"]

Example 2:
    Input: currentState = "+"
    Output: []

Constraints:
    1 <= currentState.length <= 500
    currentState[i] is either '+' or '-'.
'''

# String Simulation

from typing import List


class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        possible_states = []

        for i in range(len(currentState) - 1):
            # Find two consecutive '+' characters.
            if currentState[i:i + 2] == "++":
                next_state = (
                    currentState[:i] +
                    "--" +
                    currentState[i + 2:]
                )
                possible_states.append(next_state)

        return possible_states


# Example usage
solution = Solution()

# Example 1
state1 = "++++"
print(solution.generatePossibleNextMoves(state1))
# Output: ['--++', '+--+', '++--']

# Example 2
state2 = "+"
print(solution.generatePossibleNextMoves(state2))
# Output: []

# Example 3
state3 = "++--++"
print(solution.generatePossibleNextMoves(state3))
# Output: ['----++', '++----']

# Example 4
state4 = "--++--"
print(solution.generatePossibleNextMoves(state4))
# Output: ['------']

# Example 5
state5 = "----"
print(solution.generatePossibleNextMoves(state5))
# Output: []
