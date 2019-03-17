
class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 1
        sum = 2
        d = {int: bool}
        for num in nums:
            if num > 0:
                sum += 1
                d[num] = True
        for i in range(1, sum):
            if i not in d:
                return i
if __name__ == "__main__":
    solution = Solution()
    print(solution.firstMissingPositive([7, 8, 9, 11, 12]))