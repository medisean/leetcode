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
    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        if m == 1 and n == 1:
            if obstacleGrid[0][0] == 0:
                return 1
            return 0

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
                else:
                    obstacleGrid[i][j] = 0
        obstacleGrid[0][0] = 1

        for i in range(0, n):
            for j in range(0, m):
                if obstacleGrid[i][j] == -1:
                    continue
                if i == 0 or j == 0:
                    if i == 0 and j == 0:
                        obstacleGrid[i][j] = 1
                    elif i == 0:
                        if j - 1 >= 0:
                            obstacleGrid[i][j] = self.getValue(i, j-1, obstacleGrid)
                        else:
                            obstacleGrid[i][j] = 1
                    else:
                        if i - 1 >= 0:
                            obstacleGrid[i][j] = self.getValue(i-1, j, obstacleGrid)
                        else:
                            obstacleGrid[i][j] = 1
                else:
                    obstacleGrid[i][j] = self.getValue(i-1, j, obstacleGrid) + self.getValue(i, j-1, obstacleGrid)
        return self.getValue(n-1, m-1, obstacleGrid)

    def getValue(self, i: int, j: int, obstacleGrid: [[int]]) -> int:
        if obstacleGrid[i][j] == -1:
            return 0
        else:
            return obstacleGrid[i][j]
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePathsWithObstacles([[1, 0]]))
    