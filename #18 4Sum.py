'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        twoSums = {}
        results = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum not in twoSums:
                    twoSums[sum] = [i, j]
                else:
                    twoSums[sum].append(i)
                    twoSums[sum].append(j)
        for key in twoSums:
            values = twoSums[key]
            if target - key in twoSums:
                indexs = twoSums[target - key]
                self.getValues(values, indexs, nums, results)    
        return results
    def getValues(self, index1es: [int], index2es: [int], nums: [int], results: [int]):
        i, j = 0, 0

        while i < len(index1es):
            i1 = index1es[i]
            i2 = index1es[i+1]
            j = 0
            while j < len(index2es):
                j1 = index2es[j]
                j2 = index2es[j+1]
                if i2 < j1 or i1 > j2:
                    result = sorted([nums[i1], nums[i2], nums[j1], nums[j2]])
                    if result not in results:
                        results.append(result)
                j += 2
            i += 2

if __name__ == '__main__':
    solution = Solution()
    print(solution.fourSum([1,0,-1,0,-2,2], 0))