'''
444. Sequence Reconstruction

Check whether the original sequence nums can be uniquely reconstructed from
the given list of subsequences.

Return True if nums is the only shortest common supersequence of seqs.

Example 1:
    Input:
        nums = [1,2,3]
        sequences = [[1,2],[1,3]]

    Output:
        False

Example 2:
    Input:
        nums = [1,2,3]
        sequences = [[1,2]]

    Output:
        False

Example 3:
    Input:
        nums = [1,2,3]
        sequences = [[1,2],[1,3],[2,3]]

    Output:
        True

Constraints:
    1 <= nums.length <= 10^4
    1 <= sequences.length <= 10^4
    1 <= sum(len(seq)) <= 10^5
    1 <= nums[i], seqs[i][j] <= 10^4
'''

# Topological Sort (Kahn's Algorithm) + Graph

from typing import List
from collections import defaultdict, deque


class Solution:
    def sequenceReconstruction(
        self,
        nums: List[int],
        sequences: List[List[int]]
    ) -> bool:

        graph = defaultdict(set)
        indegree = defaultdict(int)

        nodes = set()

        # Build graph.
        for sequence in sequences:
            for value in sequence:
                nodes.add(value)

            for index in range(len(sequence) - 1):
                u = sequence[index]
                v = sequence[index + 1]

                if v not in graph[u]:
                    graph[u].add(v)
                    indegree[v] += 1

        # Every number in nums must appear.
        if nodes != set(nums):
            return False

        queue = deque()

        for value in nums:
            if indegree[value] == 0:
                queue.append(value)

        reconstructed = []

        while queue:
            # More than one choice ⇒ reconstruction is not unique.
            if len(queue) > 1:
                return False

            node = queue.popleft()
            reconstructed.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return reconstructed == nums


# Example usage
solution = Solution()

# Example 1
nums1 = [1,2,3]
seqs1 = [[1,2],[1,3]]
print(solution.sequenceReconstruction(nums1, seqs1))
# Output: False

# Example 2
nums2 = [1,2,3]
seqs2 = [[1,2]]
print(solution.sequenceReconstruction(nums2, seqs2))
# Output: False

# Example 3
nums3 = [1,2,3]
seqs3 = [[1,2],[1,3],[2,3]]
print(solution.sequenceReconstruction(nums3, seqs3))
# Output: True

# Example 4
nums4 = [4,1,5,2,6,3]
seqs4 = [[5,2,6,3],[4,1,5,2]]
print(solution.sequenceReconstruction(nums4, seqs4))
# Output: True

# Example 5
nums5 = [1]
seqs5 = [[1]]
print(solution.sequenceReconstruction(nums5, seqs5))
# Output: True

# Example 6
nums6 = [1,2,3,4]
seqs6 = [[1,2],[2,3],[2,4]]
print(solution.sequenceReconstruction(nums6, seqs6))
# Output: False
