class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check squares
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                nums = set([f'{i + 1}' for i in range(9)])
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if board[x][y] != '.' and board[x][y] not in nums:
                            return False
                        elif board[x][y] != '.':
                            nums.remove(board[x][y])
        
        # check columns
        for i in range(9):
            nums = set([f'{i + 1}' for i in range(9)])
            for j in range(9):
                if board[j][i] != '.' and board[j][i] not in nums:
                    return False
                elif board[j][i] != '.':
                    nums.remove(board[j][i])

        # check rows
        for i in range(9):
            nums = set([f'{i + 1}' for i in range(9)])
            for j in range(9):
                if board[i][j] != '.' and board[i][j] not in nums:
                    return False
                elif board[i][j] != '.':
                    nums.remove(board[i][j])

        return True
        