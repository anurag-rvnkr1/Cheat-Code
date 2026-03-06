'''
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
    Input: num1 = "2", num2 = "3"
    Output: "6"

Example 2:
    Input: num1 = "123", num2 = "456"
    Output: "56088"
 
Constraints:
    1 <= num1.length, num2.length <= 200
    num1 and num2 consist of digits only.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.
'''
# Digit Array with Carry Handling
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if num1 == "0" or num2 == "0":
            return "0"
        
        n, m = len(num1), len(num2)
        ans = [0] * (n + m)
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                
                product = digit1 * digit2
                
                pos1 = i + j
                pos2 = i + j + 1
                
                sum_val = product + ans[pos2]
                
                ans[pos2] = sum_val % 10
                ans[pos1] += sum_val // 10
        
        result = "".join(map(str, ans)).lstrip("0")
        return result

#Example usage:
solution = Solution()
print(solution.multiply("2", "3"))  # Output: "6"