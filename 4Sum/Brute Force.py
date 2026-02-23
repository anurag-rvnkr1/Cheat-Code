'''
18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target
    You may return the answer in any order.

Example 1:
    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
    Input: nums = [2,2,2,2,2], target = 8
    Output: [[2,2,2,2]]
 
Constraints:
    1 <= nums.length <= 200
    -109 <= nums[i] <= 109
    -109 <= target <= 109
'''
#brute force approach
class Solution:
    def fourSum(self, nums, target):

        n = len(nums)
        nums.sort()

        result = set()   # to avoid duplicates

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):

                        total = nums[i] + nums[j] + nums[k] + nums[l]

                        if total == target:
                            result.add((nums[i], nums[j], nums[k], nums[l]))

        return list(result)
#Example usage
solution = Solution()
print(solution.fourSum([1,0,-1,0,-2,2], 0))  # Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(solution.fourSum([2,2,2,2,2], 8))  # Output: [[2,2,2,2]]