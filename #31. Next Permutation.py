'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1


'''

class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]: # sort
                k = i + 1
                for j in range(i+2, len(nums)):
                    if nums[j] > nums[i] and nums[j] < nums[k]:
                        k = j
                nums[i], nums[k] = nums[k], nums[i] #change
                print(nums)
                nums[i+1:].sort()
        nums.reverse()
        print(nums)

if __name__ == '__main__':
    solution = Solution()
    solution.nextPermutation([1, 2])