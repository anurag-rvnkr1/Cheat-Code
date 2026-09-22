'''
433. Minimum Genetic Mutation

A gene string consists of 8 characters, where each character is one of:
    'A', 'C', 'G', 'T'

A mutation changes exactly one character.

Given:
    startGene
    endGene
    bank (valid genes)

Return the minimum number of mutations needed to transform startGene into endGene.

Each intermediate mutation must exist in the bank.

Return -1 if no valid mutation sequence exists.

Example 1:
    Input:
        startGene = "AACCGGTT"
        endGene = "AACCGGTA"
        bank = ["AACCGGTA"]

    Output:
        1

Example 2:
    Input:
        startGene = "AACCGGTT"
        endGene = "AAACGGTA"
        bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]

    Output:
        2

Example 3:
    Input:
        startGene = "AAAAACCC"
        endGene = "AACCCCCC"
        bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]

    Output:
        3

Constraints:
    startGene.length == endGene.length == 8
    0 <= bank.length <= 10
    bank[i].length == 8
'''

# BFS + Graph Traversal

from typing import List
from collections import deque


class Solution:
    def minMutation(
        self,
        startGene: str,
        endGene: str,
        bank: List[str]
    ) -> int:

        bank_set = set(bank)

        if endGene not in bank_set:
            return -1

        queue = deque([(startGene, 0)])
        visited = {startGene}

        genes = ["A", "C", "G", "T"]

        while queue:
            current_gene, mutations = queue.popleft()

            if current_gene == endGene:
                return mutations

            gene_list = list(current_gene)

            for index in range(8):
                original = gene_list[index]

                for gene in genes:
                    if gene == original:
                        continue

                    gene_list[index] = gene
                    next_gene = "".join(gene_list)

                    if (
                        next_gene in bank_set and
                        next_gene not in visited
                    ):
                        visited.add(next_gene)
                        queue.append((next_gene, mutations + 1))

                gene_list[index] = original

        return -1


# Example usage
solution = Solution()

# Example 1
start1 = "AACCGGTT"
end1 = "AACCGGTA"
bank1 = ["AACCGGTA"]

print(solution.minMutation(start1, end1, bank1))
# Output: 1

# Example 2
start2 = "AACCGGTT"
end2 = "AAACGGTA"
bank2 = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

print(solution.minMutation(start2, end2, bank2))
# Output: 2

# Example 3
start3 = "AAAAACCC"
end3 = "AACCCCCC"
bank3 = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

print(solution.minMutation(start3, end3, bank3))
# Output: 3

# Example 4
start4 = "AACCGGTT"
end4 = "AACCGCTA"
bank4 = ["AACCGGTA", "AACCGCTA"]

print(solution.minMutation(start4, end4, bank4))
# Output: 2

# Example 5
start5 = "AAAAAAAA"
end5 = "CCCCCCCC"
bank5 = ["AAAAAAAC", "AAAAAACC", "AAAACCCC", "AACCCCCC"]

print(solution.minMutation(start5, end5, bank5))
# Output: -1

# Example 6
start6 = "AACCTTGG"
end6 = "AATTCCGG"
bank6 = [
    "AACCTCGG",
    "AATCTCGG",
    "AATCTTGG",
    "AATTTTGG",
    "AATTTCGG",
    "AATTCCGG"
]

print(solution.minMutation(start6, end6, bank6))
# Output: 4
