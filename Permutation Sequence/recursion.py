"""
60. Permutation Sequence

The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

 

Example 1:
Input: n = 3, k = 3
Output: "213"


Example 2:
Input: n = 4, k = 9
Output: "2314"

Example 3:
Input: n = 3, k = 1
Output: "123"
 

Constraints:

1 <= n <= 9
1 <= k <= n!
"""

#recurssion method

class Solution:
    def getPermutation(self, n, k):

        # Available numbers
        numbers = list(range(1, n + 1))

        # Convert k to 0-based index
        k -= 1

        result = []

        # Build the permutation one position at a time
        for i in range(n):

            # Number of permutations for each fixed choice
            factorial = 1

            for j in range(1, n - i):
                factorial *= j

            # Find which number belongs at this position
            index = k // factorial

            result.append(str(numbers[index]))

            # Remove the selected number
            numbers.pop(index)

            # Move to the next group
            k %= factorial

        return ''.join(result)
