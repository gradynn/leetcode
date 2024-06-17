class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        count = 0
        x, y = 0, 0
        dx, dy = 1, 0
        out = []
        while count < m * n:
            out.append(matrix[y][x])
            matrix[y][x] = None
            if (dx != 0) and (x == n - 1 or matrix[y][x + dx] == None):
                if dx > 0:
                    dy = 1
                elif dx < 0:
                    dy = -1
                dx = 0
            elif (dy != 0) and (y == m - 1 or matrix[y + dy][x] == None):
                if dy > 0:
                    dx = -1
                elif dy < 0:
                    dx = 1
                dy = 0
            x, y = x + dx, y + dy
            count += 1
            
        return out