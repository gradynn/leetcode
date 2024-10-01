class Solution:
    def mySqrt(self, x: int) -> int:
        root = 0
        for n in range(x + 1):
            if (n * n) <= x:
                root = n
            else:
                break
        return root