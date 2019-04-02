'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        d = {}
        for s in strs:
            r = ''.join(sorted(list(s)))
            if r in d:
                c = d[r]
                c.append(s)
            else:
                d[r] = [s]
        results = []
        for key in d:
            results.append(d[key])
        return results

if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))