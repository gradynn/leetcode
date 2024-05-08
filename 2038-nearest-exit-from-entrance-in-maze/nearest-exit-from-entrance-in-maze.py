class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = [[False] * n for _ in range(m)]
        visited[entrance[0]][entrance[1]] = True

        while queue:
            row, col, level = queue.popleft()

            if (row in {0, m - 1} or col in {0, n - 1}) and [row, col] != entrance:
                return level

            for dRow, dCol in directions:
                nRow, nCol = row + dRow, col + dCol
                if nRow in range(m) and nCol in range(n) and not visited[nRow][nCol] and maze[nRow][nCol] == '.':
                    visited[nRow][nCol] = True
                    queue.append((nRow, nCol, level + 1))
            
        return -1