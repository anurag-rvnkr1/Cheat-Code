'''
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9

Constraints:
    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105
'''
#Prefix Arrays
class Solution:
    def trap(self, height):
        n = len(height)
        
        left_max = [0] * n
        right_max = [0] * n
        
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        water = 0
        
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]
        
        return water
    
#Example usage
solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
print(solution.trap([4,2,0,3,2,5]))  # Output: 9