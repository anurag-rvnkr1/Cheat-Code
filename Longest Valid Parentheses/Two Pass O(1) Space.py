'''
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

Example 1:
    Input: s = "(()"
    Output: 2
    Explanation: The longest valid parentheses substring is "()".

Example 2:
    Input: s = ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()".

Example 3:
    Input: s = ""
    Output: 0
 
Constraints:
    0 <= s.length <= 3 * 104
    s[i] is '(', or ')'.
'''
#Two Pass O(1) Space Solution
def longestValidParentheses(s):
    left = right = 0
    max_len = 0
    
    # Left to right
    for char in s:
        if char == '(':
            left += 1
        else:
            right += 1
        
        if left == right:
            max_len = max(max_len, 2 * right)
        elif right > left:
            left = right = 0
    
    left = right = 0
    
    # Right to left
    for char in reversed(s):
        if char == ')':
            right += 1
        else:
            left += 1
        
        if left == right:
            max_len = max(max_len, 2 * left)
        elif left > right:
            left = right = 0
    
    return max_len

#Example Usage
print(longestValidParentheses("(()")) # Output: 2
print(longestValidParentheses(")()())")) # Output: 4