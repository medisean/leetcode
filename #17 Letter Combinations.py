'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numberDict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        words = []
        result = []
        count = 1
        for digit in digits:
            word = numberDict[digit]
            count *= len(word)
            words.append(word)
        for i in range(count):
            result.append(111)
            
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations('234'))