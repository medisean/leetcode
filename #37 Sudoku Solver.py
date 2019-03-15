'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# 1.搜索未知的元素
# 2.是否有唯一解（查找相应地一行，相应地一列，相应地3*3）
# 3.

'''

class Solution:
    def solveSudoku(self, board: [[str]]) -> None:
        # 找出所有有未知元素
        unknown = []
        for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] == ".":
                        unknown.append([i, j])
        
        tempBoard = [] # temp board
        tempUnknown = [] # temp unknown
        tempQueue = [] # multiply results queue

        while len(unknown) != 0:
            oneAnswer = False
            for i in range(len(unknown)):
                item = unknown[i]
                results = self.answers(self.getRelated(item, board))
                # print(results)
                if len(results) == 0: # return to last status
                    board = tempBoard.copy()
                    unknown = tempUnknown.copy()

                    tempBoard = []
                    tempUnknown = []
                elif len(results) == 1: # first find all only one answer 
                    oneAnswer = True
                    board[item[0]][item[1]] = results[0]
                    unknown.pop(i)
                    break
                else: # add to temp queue
                    for result in results:
                        tempQueue.append([result, item])

            print("****************")
            if not oneAnswer:
                tempBoard = board.copy()
                tempUnknown = unknown.copy()

                guess = tempQueue[0][0] # guess first result value and pop, if wrong, guess next next time
                item = tempQueue[0][1] # position in board
                board[item[0]][item[1]] = guess
                tempQueue[0].pop(0) # remove guess、
        print(board)
                

    def getRelated(self, indexes: [int], board: [[str]]) -> [str]:
        print("board:", board)
        results = []
        for i in range(len(board)): # row
            if i == indexes[0]:
                results += board[i]
        
        for j in range(len(board)): #column
            results.append(board[j][indexes[1]])
        
        row = int(indexes[0] / 3)
        column = int(indexes[1] / 3)

        for i in range(3): # 3*3
            for j in range(3):
                print(i+row*3, j+column*3)
                results.append(board[i+row*3][j+column*3]) 
        return results
    
    def answers(self, strs: [str]) -> [str]:
        arrs = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        return [elem for elem in arrs if elem != "." and elem not in strs]

if __name__ == "__main__":
    solution = Solution()
    # print(solution.solveSudoku([
    #     ["5","3",".",".","7",".",".",".","."],
    #     ["6",".",".","1","9","5",".",".","."],
    #     [".","9","8",".",".",".",".","6","."],
    #     ["8",".",".",".","6",".",".",".","3"],
    #     ["4",".",".","8",".","3",".",".","1"],
    #     ["7",".",".",".","2",".",".",".","6"],
    #     [".","6",".",".",".",".","2","8","."],
    #     [".",".",".","4","1","9",".",".","5"],
    #     [".",".",".",".","8",".",".","7","9"]]))
    print(solution.solveSudoku([
        [".",".","9","7","4","8",".",".","."],
        ["7",".",".",".",".",".",".",".","."],
        [".","2",".","1",".","9",".",".","."],
        [".",".","7",".",".",".","2","4","."],
        [".","6","4",".","1",".","5","9","."],
        [".","9","8",".",".",".","3",".","."],
        [".",".",".","8",".","3",".","2","."],
        [".",".",".",".",".",".",".",".","6"],
        [".",".",".","2","7","5","9",".","."]]))

        