'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
'''

class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        d = {"1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False}
        for row in board: # check row
            for column in row:
                if column != ".":
                    if d[column] == True:
                        return False
                    else:
                        d[column] = True
            for key in d: # reset status
                d[key] = False 

        for i in range(len(board)): # check column
            for j in range(len(board)):
                if board[j][i] != ".":
                    if d[board[j][i]] == True:
                        return False
                    else:
                        d[board[j][i]] = True
            for key in d:
                d[key] = False # reset status
        
        print("ready")
        for i in range(3): # check 3*3 matrix
            rows = board[i*3:(i+1)*3]
            for j in range(3):
                results = []
                for row in rows:
                    results += row[j*3:(j+1)*3]
                if not self.isArrayValid(results):
                    return False
        return True
    
    def isArrayValid(self, strs: [str]) -> bool:
        d = {"1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False}
        for s in strs:
            if s != ".":
                if d[s] == True:
                    return False
                else:
                    d[s] = True
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isValidSudoku([
        [".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."]]))