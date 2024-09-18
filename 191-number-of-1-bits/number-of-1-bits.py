class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(n.bit_length()):
            count += (n & 1)
            n >>= 1
        return count