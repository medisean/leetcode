#!/usr/bin/python3

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        for i in range(int(len(s)/2)):
            last = len(s) - i - 1
            if s[i] != s[last]:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(121))