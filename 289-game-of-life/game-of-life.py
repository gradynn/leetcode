class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        new_board = [[0 for i in range(m)] for j in range(n)]
        
        for i in range(n):
            for j in range(m):
                cell = board[i][j]
                
                live_neighbors = 0
                for y in range(max(i - 1, 0), min(i + 2, n)):
                    for x in range(max(j - 1, 0), min(j + 2, m)):
                            live_neighbors += board[y][x]
                live_neighbors -= board[i][j]

                if cell:
                    new_board[i][j] = live_neighbors == 2 or live_neighbors == 3
                else:
                    new_board[i][j] = live_neighbors == 3

        for i in range(n):
            for j in range(m):
                board[i][j] = int(new_board[i][j])
        