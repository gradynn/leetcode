class Solution:
    def numTilings(self, n: int) -> int:
        full = [0, 1, 2]
        topMissing = [0, 0, 1]
        bottomMissing = [0, 0, 1]

        for i in range(3, n + 1):
            full.append(full[i - 1] + full[i - 2] + topMissing[i - 1] + bottomMissing[i - 1])
            topMissing.append(bottomMissing[i - 1] + full[i - 2])
            bottomMissing.append(topMissing[i - 1] + full[i - 2])

        return full[n] % ((10 ** 9) + 7)