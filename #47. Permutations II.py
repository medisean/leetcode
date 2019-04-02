'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

排列组合算法   3！ = 6
'''
class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        results = []
        for i in range(len(nums)):
            if i == 0:
                results.append([nums[i]])
            else:
                z = []
                for r in results:
                    for k in range(len(r)):
                        t = r.copy()
                        t.insert(k, nums[i])
                        if t not in z:
                            z.append(t)
                    t = r.copy()
                    t.append(nums[i])
                    if t not in z:
                        z.append(t)
                results = z
        return results

if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 1]))
        