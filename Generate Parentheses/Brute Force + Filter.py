'''
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
    Input: n = 1
    Output: ["()"]
    
Constraints:
    1 <= n <= 8
'''
#Brute Force + Filter
class Solution:
    def generateParenthesis(self, n):

        result = []

        def generate(curr):
            # If length is 2n, check validity
            if len(curr) == 2 * n:
                if self.isValid(curr):
                    result.append(curr)
                return

            generate(curr + '(')
            generate(curr + ')')

        generate("")
        return result

    def isValid(self, s):

        balance = 0

        for ch in s:
            if ch == '(':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                return False

        return balance == 0
    
#Example usage
solution = Solution()
print(solution.generateParenthesis(3))  # Output: ["((()))","(()())","(())()","()(())","()()()"]
print(solution.generateParenthesis(1))  # Output: ["()"]