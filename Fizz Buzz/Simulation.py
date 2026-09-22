'''
412. Fizz Buzz

Given an integer n, return a string array answer (1-indexed) where:

    - answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    - answer[i] == "Fizz" if i is divisible by 3.
    - answer[i] == "Buzz" if i is divisible by 5.
    - answer[i] == str(i) otherwise.

Example 1:
    Input:
        n = 3

    Output:
        ["1","2","Fizz"]

Example 2:
    Input:
        n = 5

    Output:
        ["1","2","Fizz","4","Buzz"]

Example 3:
    Input:
        n = 15

    Output:
        ["1","2","Fizz","4","Buzz","Fizz","7","8",
         "Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Constraints:
    1 <= n <= 10^4
'''

# Simulation

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for number in range(1, n + 1):
            if number % 15 == 0:
                result.append("FizzBuzz")
            elif number % 3 == 0:
                result.append("Fizz")
            elif number % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(number))

        return result


# Example usage
solution = Solution()

# Example 1
n1 = 3
print(solution.fizzBuzz(n1))
# Output: ["1","2","Fizz"]

# Example 2
n2 = 5
print(solution.fizzBuzz(n2))
# Output: ["1","2","Fizz","4","Buzz"]

# Example 3
n3 = 15
print(solution.fizzBuzz(n3))
# Output:
# ["1","2","Fizz","4","Buzz","Fizz","7","8",
#  "Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

# Example 4
n4 = 1
print(solution.fizzBuzz(n4))
# Output: ["1"]

# Example 5
n5 = 20
print(solution.fizzBuzz(n5))
# Output:
# ["1","2","Fizz","4","Buzz","Fizz","7","8",
#  "Fizz","Buzz","11","Fizz","13","14","FizzBuzz",
#  "16","17","Fizz","19","Buzz"]

# Example 6
n6 = 30
print(solution.fizzBuzz(n6))
# Output: Standard FizzBuzz sequence up to 30.
