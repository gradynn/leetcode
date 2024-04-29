class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        waysToReach = [[0] * n for i in range(m)]
        for i in range(n):
            waysToReach[0][i] = 1
        for i in range(m):
            waysToReach[i][0] = 1
        
        for row in range(1, m):
            for col in range(1, n):
                waysToReach[row][col] = waysToReach[row][col - 1] + waysToReach[row - 1][col]

        return waysToReach[m - 1][n - 1]