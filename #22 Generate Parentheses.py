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
        results = ['(']
        temp = []
        for i in range(1, 2*n):
            temp = []
            for result in results:
                if result.count("(")  < n and result.count(")")  < n:
                    temp.append(result + "(")
                    temp.append(result + ")")
                elif result.count("(")  < n:
                    temp.append(result + "(")
                else:
                    temp.append(result + ")")
            results = temp
        temp = []
        for result in results:
            if self.isValid(result):
                temp.append(result)
        return temp
    
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            elif stack[-1] == "(":
                if c == "(":
                    stack.append("(")
                else:
                    stack.pop(-1)
            elif stack[-1] == ")":
                return False
        if len(stack) == 0:
            return True
        else:
            return False
                
    

if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))