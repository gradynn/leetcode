class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # for each layer floor(n / 2)
        for i in range(n // 2):
            print(f'Layer {i}')
            # swap from top
            print('TOP')
            for j in range(i, n - 1 - i):
                print(f'- Swapping matrix[{i}][{j}] and matrix[{j}][{n - 1 - i}]')
                matrix[i][j], matrix[j][n - 1 - i] = matrix[j][n - 1 - i], matrix[i][j]

            # swap from left
            print('LEFT')
            for j in range(n - 1 - i, i, -1):
                print(f'- Swapping matrix[{j}][{i}] and matrix[{i}][{n - j - 1}]')
                matrix[j][i], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[j][i]

            # swap from bottom
            print('BOTTOM')
            for j in range(n - 1 - i, i, -1):
                print(f'- Swapping matrix[{n - 1- i}][{j}] and matrix[{j}][{i}]')
                matrix[n - 1 - i][j], matrix[j][i] = matrix[j][i], matrix[n - 1 - i][j]