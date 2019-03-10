'''
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
'''
class Solution:
    def findSubstring(self, s: str, words: [str]) -> [int]:
        if len(words) == 0:
            return []
        
        wordLen = len(words[0])
        longWordsLen = wordLen * len(words)
        result = []
        for i in range(len(s) - longWordsLen + 1):
            flag = True
            current = s[i : i + longWordsLen]
            for j in range(len(words)):
                index = -1
                for k in range(len(words)):
                    if current[k*wordLen:(k+1)*wordLen] == words[j]:
                        index = k*wordLen
                        break
                if index == -1:
                    flag = False
                    break
                else:
                    current = current[0:index] + current[index+wordLen:]
            if flag and i not in result:
                result.append(i)
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.findSubstring('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word']))
