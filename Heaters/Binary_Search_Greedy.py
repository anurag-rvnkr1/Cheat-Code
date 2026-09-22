'''
475. Heaters

Winter is coming. You have houses and heaters on a horizontal line.

Each heater warms every house within a fixed radius.

Return the minimum radius required so that every house is covered by at least
one heater.

Example 1:
    Input:
        houses = [1,2,3]
        heaters = [2]

    Output:
        1

Example 2:
    Input:
        houses = [1,2,3,4]
        heaters = [1,4]

    Output:
        1

Example 3:
    Input:
        houses = [1,5]
        heaters = [2]

    Output:
        3

Constraints:
    1 <= houses.length, heaters.length <= 3 * 10^4
    1 <= houses[i], heaters[i] <= 10^9
'''

# Binary Search + Greedy

from typing import List
import bisect


class Solution:
    def findRadius(
        self,
        houses: List[int],
        heaters: List[int]
    ) -> int:

        heaters.sort()
        minimum_radius = 0

        for house in houses:
            position = bisect.bisect_left(heaters, house)

            left_distance = float("inf")
            right_distance = float("inf")

            if position > 0:
                left_distance = house - heaters[position - 1]

            if position < len(heaters):
                right_distance = heaters[position] - house

            nearest_heater = min(left_distance, right_distance)
            minimum_radius = max(minimum_radius, nearest_heater)

        return minimum_radius


# Example usage
solution = Solution()

# Example 1
houses1 = [1,2,3]
heaters1 = [2]
print(solution.findRadius(houses1, heaters1))
# Output: 1

# Example 2
houses2 = [1,2,3,4]
heaters2 = [1,4]
print(solution.findRadius(houses2, heaters2))
# Output: 1

# Example 3
houses3 = [1,5]
heaters3 = [2]
print(solution.findRadius(houses3, heaters3))
# Output: 3

# Example 4
houses4 = [1,10,20]
heaters4 = [2,15]
print(solution.findRadius(houses4, heaters4))
# Output: 5

# Example 5
houses5 = [5]
heaters5 = [1,2,3,4,5]
print(solution.findRadius(houses5, heaters5))
# Output: 0

# Example 6
houses6 = [2,4,6,8]
heaters6 = [1,5,9]
print(solution.findRadius(houses6, heaters6))
# Output: 2
