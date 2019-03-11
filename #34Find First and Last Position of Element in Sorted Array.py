'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''
class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        first = -1
        last = -1
        for i in range(int((len(nums) + 1)/2)):
            if nums[i] == target:
                if first == -1:
                    first = i
                elif first > i:
                    first = i
                if last == -1:
                    last = i
                elif last < i:
                    last = i
            if nums[len(nums) - i - 1] == target:
                if last == -1:
                    last = len(nums) - i - 1
                elif last < len(nums) - i - 1:
                    last = len(nums) - i - 1
                if first == -1:
                    first = len(nums) - i - 1
                elif first > len(nums) - i - 1:
                    first = len(nums) - i - 1
        return [first, last]

if __name__ == '__main__':
    solution = Solution()
    print(solution.searchRange([1,2,2,3,4,4,4], 3))