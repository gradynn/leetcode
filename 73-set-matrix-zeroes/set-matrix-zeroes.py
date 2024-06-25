class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        # sweep and collect rows/column indeces in set
        rows = set()
        columns = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)

        # set all rows, columns to 0
        for row in rows:
            for i in range(m):
                matrix[row][i] = 0
        for column in columns:
            for i in range(n):
                matrix[i][column] = 0
        