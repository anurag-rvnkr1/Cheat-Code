'''
Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
    Input: x = 123
    Output: 321

Example 2:
    Input: x = -123
    Output: -321
Example 3:
    Input: x = 120
    Output: 21
 
Constraints:
    -231 <= x <= 231 - 1

'''
#Math Method
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x:
            d = x % 10
            x //= 10

            if res > INT_MAX // 10 or (res == INT_MAX // 10 and d > 7):
                return 0

            res = res * 10 + d

        return sign * res
    
#Example Usage
solution = Solution()
print(solution.reverse(123))  # Output: 321
print(solution.reverse(-123)) # Output: -321