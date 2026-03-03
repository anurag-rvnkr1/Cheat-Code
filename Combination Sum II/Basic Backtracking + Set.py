'''
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:
    Input: candidates = [10,1,2,7,6,1,5], target = 8
    Output: 
    [
    [1,1,6],
    [1,2,5],
    [1,7],
    [2,6]
    ]

Example 2:
    Input: candidates = [2,5,2,1,2], target = 5
    Output: 
    [
    [1,2,2],
    [5]
    ]
 
Constraints:
    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30
'''
#Basic Backtracking + Set
class Solution:
    def combinationSum2(self, candidates, target):
        result = set()
        
        def backtrack(start, current, remaining):
            if remaining == 0:
                result.add(tuple(sorted(current)))
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i + 1, current, remaining - candidates[i])
                current.pop()
        
        backtrack(0, [], target)
        return [list(comb) for comb in result]

#Example usage
sol=Solution()
print(sol.combinationSum2([10,1,2,7,6,1,5], 8))
print(sol.combinationSum2([2,5,2,1,2], 5))