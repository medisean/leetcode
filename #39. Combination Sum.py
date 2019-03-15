'''

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        ans = []
        results = []
        for c in candidates:
            results.append([c, [c]])

        while len(results) != 0:
            first = results[0]
            results.pop(0)
            if first[0] == target:
                t = sorted(first[1])
                if t not in ans:
                    ans.append(t)
                    continue
            for c in candidates:
                temp = first.copy()
                if c + temp[0] <= target:
                    temp[0] = c + temp[0]
                    arr = temp[1].copy()
                    arr.append(c)
                    results.append([temp[0], arr])
        return ans

if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum([8, 7, 4, 3], 11))