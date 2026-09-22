'''
401. Binary Watch

A binary watch has 4 LEDs for hours (0-11) and 6 LEDs for minutes (0-59).

Given an integer turnedOn representing the number of LEDs that are currently on,
return all possible times the watch could represent.

Hours must not contain a leading zero.
Minutes must always be two digits.

Example 1:
    Input:
        turnedOn = 1

    Output:
        ["0:01","0:02","0:04","0:08","0:16","0:32",
         "1:00","2:00","4:00","8:00"]

Example 2:
    Input:
        turnedOn = 9

    Output:
        []

Constraints:
    0 <= turnedOn <= 10
'''

# Backtracking + Bit Manipulation

from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []

        for hour in range(12):
            for minute in range(60):
                if (
                    hour.bit_count() +
                    minute.bit_count()
                ) == turnedOn:
                    result.append(f"{hour}:{minute:02d}")

        return result


# Example usage
solution = Solution()

# Example 1
turnedOn1 = 1
print(solution.readBinaryWatch(turnedOn1))
# Output:
# ['0:01','0:02','0:04','0:08','0:16','0:32',
#  '1:00','2:00','4:00','8:00']

# Example 2
turnedOn2 = 9
print(solution.readBinaryWatch(turnedOn2))
# Output: []

# Example 3
turnedOn3 = 0
print(solution.readBinaryWatch(turnedOn3))
# Output: ['0:00']

# Example 4
turnedOn4 = 2
print(solution.readBinaryWatch(turnedOn4))
# Output: All valid times with exactly 2 LEDs on.

# Example 5
turnedOn5 = 3
print(solution.readBinaryWatch(turnedOn5))
# Output: All valid times with exactly 3 LEDs on.

# Example 6
turnedOn6 = 10
print(solution.readBinaryWatch(turnedOn6))
# Output: []
