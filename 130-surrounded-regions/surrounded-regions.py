class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        connected = set()

        rows, cols = len(board), len(board[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            connected.add((r, c))

            while q:
                row, col = q.pop()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    nRow, nCol = row + dr, col + dc
                    if (nRow in range(rows) and
                        nCol in range(cols) and
                        (nRow, nCol) not in connected and 
                        board[nRow][nCol] == "O"):
                        q.append((nRow, nCol))
                        connected.add((nRow, nCol))

        for i in range(cols):
            if board[0][i] == "O":
                bfs(0, i)
            if board[rows - 1][i] == "O":
                bfs(rows - 1, i)
        for i in range(1, rows - 1):
            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][cols - 1] == "O":
                bfs(i, cols - 1)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row, col) not in connected:
                    board[row][col] = "X"