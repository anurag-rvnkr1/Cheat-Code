'''
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

Example 3:
    Input: nums = [1], target = 0
    Output: -1

Constraints:
    1 <= nums.length <= 5000
    -104 <= nums[i] <= 104
    All values of nums are unique.
    nums is an ascending array that is possibly rotated.
    -104 <= target <= 104
'''
#Find the pivot and then do normal binary search
def search(nums, target):
    if not nums:
        return -1
    
    n = len(nums)
    
    # Step 1: Find pivot (smallest element)
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    pivot = left
    
    # Step 2: Normal binary search with adjusted indices
    left, right = 0, n - 1
    
    while left <= right:
        mid = (left + right) // 2
        real_mid = (mid + pivot) % n
        
        if nums[real_mid] == target:
            return real_mid
        elif nums[real_mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
#Example usage
print(search([4,5,6,7,0,1,2], 0))  # Output: 4