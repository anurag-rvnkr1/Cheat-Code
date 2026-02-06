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
#String Method
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        s = str(abs(x))[::-1]
        num = sign * int(s)

        if num < -2**31 or num > 2**31 - 1:
            return 0
        return num
    
#Example Usage
sol = Solution()
print(sol.reverse(123))    # Output: 321
print(sol.reverse(-123))   # Output: -321