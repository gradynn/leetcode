class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nRow, nCol = row + dr, col + dc
                    if (nRow in range(rows) and
                        nCol in range(cols) and
                        grid[nRow][nCol] == "1" and 
                        (nRow, nCol) not in visited):
                        q.append((nRow, nCol))
                        visited.add((nRow, nCol))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1

        return islands
        