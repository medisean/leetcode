'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        if len(matrix) == 0:
            return []

        direction = 0 # 0: right, 1: down, 2: left, 3: up
        m = len(matrix)
        n = len(matrix[0])
        result = []
        j, k = 0, 0
        r, b, l, u = n, m, 0, 0
        for _ in range(m*n):
            result.append(matrix[j][k])
            if direction == 0:
                if k + 1 < r:
                    k += 1
                else:
                    u += 1
                    j += 1
                    direction = 1
            elif direction == 1:
                if j + 1 < b:
                    j += 1
                else:
                    r -= 1
                    k -= 1
                    direction = 2
            elif direction == 2:
                if k - 1 >= l:
                    k -= 1
                else:
                    j -= 1
                    b -= 1
                    direction = 3
            elif direction == 3:
                if j - 1 >= u:
                    j -= 1
                else:
                    l += 1
                    k += 1
                    direction = 0
        return result

if __name__ == '__main__':
    solution = Solution()
    solution.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
])