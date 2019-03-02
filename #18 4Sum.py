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
        twoSumAboveZero = []
        twoSumBelowZero = []
        twoSumEqualZero = []
        results = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum > 0:
                    twoSumAboveZero.append([i, j, sum])
                elif sum == 0:
                    twoSumEqualZero.append([i, j, sum])
                else:
                    twoSumBelowZero.append([i, j, sum])

        for sum in twoSumAboveZero:
            filters = filter(lambda x: (sum[1] < x[0] or sum[0] > x[1]) and x[2] == target-sum[2], twoSumBelowZero)
            for t in filters:
                result = sorted([nums[sum[0]], nums[sum[1]], nums[t[0]], nums[t[1]]])
                if result not in results:
                    results.append(result)
        for sum in twoSumEqualZero:
            filters = filter(lambda x: sum[1] < x[0] and x[2] == target-sum[2], twoSumEqualZero)
            for t in filters:
                result = sorted([nums[sum[0]], nums[sum[1]], nums[t[0]], nums[t[1]]])
                if result not in results:
                    results.append(result)
        return results

if __name__ == '__main__':
    solution = Solution()
    print(solution.fourSum([-3,-1,0,2,4,5], 0))