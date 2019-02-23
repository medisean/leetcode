'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''
class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if len(strs) == 0:
            return ''

        result = ''
        maxLength = len(strs[0])
        for str in strs:
            if len(str) < maxLength:
                maxLength = len(str)
        for i in range(maxLength):
            c = strs[0][i]
            for str in strs:
                if str[i] != c:
                    return result
            result += c
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["flower","flow","flight"]))