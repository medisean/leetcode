'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
'''

class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isValidSudoku([]))