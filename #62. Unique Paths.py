'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        s = [[0] * m] * n
        s[0][0] = 1

        for i in range(0, n):
            for j in range(0, m):
                if i == 0 or j == 0:
                    if i == 0 and j == 0:
                        s[i][j] = 1
                    elif i == 0:
                        if j - 1 >= 0:
                            s[i][j] = s[i][j-1] 
                        else:
                            s[i][j] = 1
                    else:
                        if i - 1 >= 0:
                            s[i][j] = s[i-1][j] 
                        else:
                            s[i][j] = 1
                else:
                    s[i][j] = s[i-1][j] + s[i][j-1]
        return s[n-1][m-1]
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePaths(3, 2))