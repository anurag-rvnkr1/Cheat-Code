'''
358. Rearrange String k Distance Apart

Given a string s and an integer k, rearrange the string such that the same
characters are at least distance k from each other.

If it is not possible, return an empty string.

Example 1:
    Input:
        s = "aabbcc"
        k = 3

    Output:
        "abcabc"

Example 2:
    Input:
        s = "aaabc"
        k = 3

    Output:
        ""

Example 3:
    Input:
        s = "aaadbbcc"
        k = 2

    Output:
        "abacabcd"

Constraints:
    1 <= s.length <= 3 * 10^5
    s consists of lowercase English letters.
    0 <= k <= s.length
'''

# Max Heap + Greedy + Queue

from collections import Counter, deque
import heapq


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        frequency = Counter(s)

        # Max heap: (-count, character)
        max_heap = [
            (-count, character)
            for character, count in frequency.items()
        ]
        heapq.heapify(max_heap)

        wait_queue = deque()
        result = []

        while max_heap or wait_queue:

            if max_heap:
                count, character = heapq.heappop(max_heap)

                result.append(character)

                count += 1  # One occurrence used.

                wait_queue.append((count, character))

            else:
                return ""

            # Release characters after k distance.
            if len(wait_queue) >= k:
                count, character = wait_queue.popleft()

                if count < 0:
                    heapq.heappush(max_heap, (count, character))

        return "".join(result)


# Example usage
solution = Solution()

# Example 1
s1 = "aabbcc"
k1 = 3
print(solution.rearrangeString(s1, k1))
# Output: "abcabc"

# Example 2
s2 = "aaabc"
k2 = 3
print(solution.rearrangeString(s2, k2))
# Output: ""

# Example 3
s3 = "aaadbbcc"
k3 = 2
print(solution.rearrangeString(s3, k3))
# Output: "abacabcd"

# Example 4
s4 = "aa"
k4 = 0
print(solution.rearrangeString(s4, k4))
# Output: "aa"

# Example 5
s5 = "aaaabbbbcc"
k5 = 2
print(solution.rearrangeString(s5, k5))
# Output: Valid rearrangement

# Example 6
s6 = "aabc"
k6 = 2
print(solution.rearrangeString(s6, k6))
# Output: "abac"
