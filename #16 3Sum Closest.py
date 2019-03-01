'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        '''
        distance = 1000000
        result = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    total = nums[i] + nums[j] + nums[k]
                    if abs(target - total) < distance:
                        distance = abs(target - total)
                        result = total
        return result
        # This method is O(n, 3), not good enough
        '''
        return 0

if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSumClosest([-1, 2, 1, -4], 1))