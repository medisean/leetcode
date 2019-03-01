'''
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        allPosible = []
        for i in range(len(s)):
            if i < len(s) - 1:
                twoc = s[i: i+2]
                if twoc[0] == twoc[1]:
                    allPosible.append([twoc, i, 2])
            allPosible.append([s[i], i, 1])
        for possible in allPosible:
            index = possible[1]
            length = possible[2]
            palindrome = possible[0]
            
        return ''

if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome('babad'))