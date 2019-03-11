'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

'''

class Solution:
    def longestValidParentheses(self, s: str) -> int: # replace () with * and count *
        results = []
        for c in s:
            results.append(c)
        
        longest = 0
        flags = []
        current = 0
        for i in range(len(results)):
            if results[i] == "(":
                flags.append(i)
                current = i
            else:
                if len(flags) != 0:
                    if current == flags[-1]:
                        results[flags[-1]] = "*"
                        results[i] = "*"
                        flags.pop(-1)     
                        if len(flags) == 0:
                            current = i + 1
                        else:
                            current = flags[-1]
                    else:
                        flags = []
                else:
                    current = i + 1

        current = 0
        for i in range(len(results)):
            if results[i] == "*":
                current += 1
                if i == len(results) - 1:
                    longest = max(current, longest)
            else:
                longest = max(current, longest)
                current = 0
        return longest

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestValidParentheses("(()"))
    