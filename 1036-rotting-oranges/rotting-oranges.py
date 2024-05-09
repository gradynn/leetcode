class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        maxDepth = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        print(q)
        while q:
            i, j, depth = q.popleft()

            maxDepth = max(maxDepth, depth)

            for di, dj in directions:
                row, col = i + di, j + dj
                if (col >= 0 and col < n) and (row >= 0 and row < m):
                    if grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row, col, depth + 1))
        
        for row in grid:
            if 1 in row:
                return -1
        return maxDepth