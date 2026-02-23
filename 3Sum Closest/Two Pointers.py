'''
16. 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
    Input: nums = [0,0,0], target = 1
    Output: 0
    Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 
Constraints:
    3 <= nums.length <= 500
    -1000 <= nums[i] <= 1000
    -104 <= target <= 104
'''
#two pointers solution
class Solution:
    def threeSumClosest(self, nums, target):

        nums.sort()
        n = len(nums)

        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):

            left = i + 1
            right = n - 1

            while left < right:

                curr_sum = nums[i] + nums[left] + nums[right]

                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum

                # Perfect match
                if curr_sum == target:
                    return curr_sum

                # Move pointers
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest

# Example usage:
solution = Solution()
print(solution.threeSumClosest([-1,2,1,-4], 1)) # Output: 2
print(solution.threeSumClosest([0,0,0], 1)) # Output: 0