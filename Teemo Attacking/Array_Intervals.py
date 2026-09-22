'''
495. Teemo Attacking

Teemo attacks Ashe multiple times. Each attack poisons Ashe for a fixed
duration. If Ashe is already poisoned when another attack happens, the poison
duration is refreshed (overlaps do not stack).

Given the attack times and poison duration, return the total time Ashe remains
poisoned.

Example 1:
    Input:
        timeSeries = [1,4]
        duration = 2

    Output:
        4

Explanation:
        Poison intervals:
        [1,3)
        [4,6)
        Total poisoned time = 2 + 2 = 4

Example 2:
    Input:
        timeSeries = [1,2]
        duration = 2

    Output:
        3

Explanation:
        Poison intervals:
        [1,3)
        [2,4)
        Union = [1,4) => 3 seconds

Constraints:
    1 <= timeSeries.length <= 10^4
    0 <= timeSeries[i] <= 10^7
    timeSeries is sorted in non-decreasing order.
    1 <= duration <= 10^7
'''

# Array + Interval Merging

from typing import List


class Solution:
    def findPoisonedDuration(
        self,
        timeSeries: List[int],
        duration: int
    ) -> int:

        if not timeSeries:
            return 0

        total_poison_time = 0

        for index in range(len(timeSeries) - 1):
            gap = timeSeries[index + 1] - timeSeries[index]

            # Overlapping intervals contribute only the gap.
            total_poison_time += min(duration, gap)

        # Last attack always contributes full duration.
        total_poison_time += duration

        return total_poison_time


# Example usage
solution = Solution()

# Example 1
timeSeries1 = [1,4]
duration1 = 2
print(solution.findPoisonedDuration(timeSeries1, duration1))
# Output: 4

# Example 2
timeSeries2 = [1,2]
duration2 = 2
print(solution.findPoisonedDuration(timeSeries2, duration2))
# Output: 3

# Example 3
timeSeries3 = [1,2,3]
duration3 = 2
print(solution.findPoisonedDuration(timeSeries3, duration3))
# Output: 4

# Example 4
timeSeries4 = [5]
duration4 = 10
print(solution.findPoisonedDuration(timeSeries4, duration4))
# Output: 10

# Example 5
timeSeries5 = [1,5,10]
duration5 = 3
print(solution.findPoisonedDuration(timeSeries5, duration5))
# Output: 9

# Example 6
timeSeries6 = [1,2,4,7]
duration6 = 3
print(solution.findPoisonedDuration(timeSeries6, duration6))
# Output: 9
