'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        result = []
        numDict = {int: int}
        for i in range(len(nums)):
            numDict[nums[i]] = i
        twoAddArray = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                first = nums[i]
                second = nums[j]
                twoAddArray.append([i, j, first+second])
        for array in twoAddArray:
            if -array[2] in numDict and numDict[-array[2]] > array[0] and numDict[-array[2]] > array[1]:
                sortedArray = [nums[array[0]], nums[array[1]], nums[numDict[-array[2]]]]
                sortedArray.sort()
                if sortedArray not in result:
                    result.append(sortedArray)
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
    print(solution.threeSum([]))