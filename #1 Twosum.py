
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        d = {int: int}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [i, d[target-nums[i]]]
            else:
                d[nums[i]] = i
        return []

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))