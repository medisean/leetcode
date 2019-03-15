
class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        d = {int: bool}
        for num in nums:
            d[num] = True
        for i in range(1, len(nums)+1):
            if i not in d:
                return i
if __name__ == "__main__":
    solution = Solution()
    print(solution.firstMissingPositive([7, 8, 9, 11, 12]))