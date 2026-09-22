'''
457. Circular Array Loop

Given a circular integer array nums, determine if there exists a cycle.

Rules for a valid cycle:
    - The cycle length must be greater than 1.
    - Movement must be entirely in one direction
      (all positive or all negative numbers).
    - The array is circular.

Return True if a valid cycle exists; otherwise False.

Example 1:
    Input:
        nums = [2,-1,1,2,2]

    Output:
        True

Example 2:
    Input:
        nums = [-1,2]

    Output:
        False

Example 3:
    Input:
        nums = [-2,1,-1,-2,-2]

    Output:
        False

Constraints:
    1 <= nums.length <= 5000
    -1000 <= nums[i] <= 1000
    nums[i] != 0
'''

# Fast & Slow Pointers (Floyd Cycle Detection)

from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(index: int) -> int:
            return (index + nums[index]) % n

        for start in range(n):
            direction = nums[start] > 0

            slow = start
            fast = start

            while True:
                # Slow pointer.
                next_slow = next_index(slow)

                if (
                    (nums[next_slow] > 0) != direction or
                    next_slow == slow
                ):
                    break

                # Fast pointer (first move).
                next_fast = next_index(fast)

                if (
                    (nums[next_fast] > 0) != direction or
                    next_fast == fast
                ):
                    break

                # Fast pointer (second move).
                next_fast2 = next_index(next_fast)

                if (
                    (nums[next_fast2] > 0) != direction or
                    next_fast2 == next_fast
                ):
                    break

                slow = next_slow
                fast = next_fast2

                if slow == fast:
                    return True

            # Mark visited nodes to avoid repeated work.
            index = start

            while (nums[index] > 0) == direction:
                next_pos = next_index(index)
                nums[index] = 0

                if next_pos == index:
                    break

                index = next_pos

        return False


# Example usage
solution = Solution()

# Example 1
nums1 = [2,-1,1,2,2]
print(solution.circularArrayLoop(nums1.copy()))
# Output: True

# Example 2
nums2 = [-1,2]
print(solution.circularArrayLoop(nums2.copy()))
# Output: False

# Example 3
nums3 = [-2,1,-1,-2,-2]
print(solution.circularArrayLoop(nums3.copy()))
# Output: False

# Example 4
nums4 = [1,1,1,1]
print(solution.circularArrayLoop(nums4.copy()))
# Output: True

# Example 5
nums5 = [-1,-2,-3,-4,-5]
print(solution.circularArrayLoop(nums5.copy()))
# Output: False

# Example 6
nums6 = [3,1,2]
print(solution.circularArrayLoop(nums6.copy()))
# Output: True
