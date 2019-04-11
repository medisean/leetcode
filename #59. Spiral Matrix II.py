'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''
class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        matrix = []
        for _ in range(n):
            row = [0 for i in range(n)]
            matrix.append(row)
        i, j = 0, 0
        d = 0 # 0: right, 1: bottom, 2: left, 3: up
        r, b, l, u = n, n, 0, 0
        for k in range(1, n*n+1):
            matrix[i][j] = k
            if d == 0:
                if j + 1 < r:
                    j += 1
                else:
                    u += 1
                    d = 1
                    i += 1
            elif d == 1:
                if i + 1 < b:
                    i += 1
                else:
                    r -= 1
                    d = 2
                    j -= 1
            elif d == 2:
                if j - 1 >= l:
                    j -= 1
                else:
                    b -= 1
                    d = 3
                    i -= 1
            elif d == 3:
                if i - 1 >= u:
                    i -= 1
                else:
                    d = 0
                    j += 1
                    l += 1
        return matrix

if __name__ == '__main__':
    solution = Solution()
    print(solution.generateMatrix(4))