class Solution:
    def bucketSort(self, nums: [int]):
        result = []
        for num in nums:
            result.append(num)
            result = self.sort(result)
        print(result)

    def sort(self, nums: [int]):
        if len(nums) <= 1:
            return nums
        else:
            if nums[-1] < nums[-2]:
                target = nums[-1] # target is 4
                nums = nums[::-1] # step 1: reverse, [4 7 6 5 2 1]
                pos = self.findPos(nums) # step 2: find position of 4 in array [7 6 5 2 1]
                temp = nums[:pos] # step 3: begin position array [4 7 6 5]
                temp = temp[::-1]  # step 4: reverse [5 6 7 4]
                temp = temp[:-1] # step 5: [5 6 7]
                temp = temp[::-1] + [target] # step 6: reverse [7 6 5] + [4] = [7 6 5 4]
                nums = temp + nums[pos:] # step 7: [7 6 5 4 2 1]
                nums = nums[::-1] # step 8: [1 2 4 5 6 7]
                return nums
            else:
                return nums
    
    def findPos(self, nums: [int]) -> int:
        for i in range(1, len(nums)):
            if nums[i] < nums[0]:
                return i

# [1 2 5 6 7] 4
# 4 7 6 5 2 1
# 5 6 7 4 2 1
# 7 6 5 4 2 1
# 1 2 4 5 6 7

if __name__ == '__main__':
    solution = Solution()
    solution.bucketSort([1, 2, 5, 6, 7, 4])