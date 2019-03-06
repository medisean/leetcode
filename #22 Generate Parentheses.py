'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

n = 2
[
  "(())"
  "()()"
]

(

((
()

(((
(()
()(
if c == (
after ( or ) 
else 
after )
'''

class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        return []

if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))