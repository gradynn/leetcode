class Solution:
    def reverseBits(self, n: int) -> int:
        b_string = bin(n)[2:]
        b_string = "0" * (32 - len(b_string)) + b_string
        b_int = int(b_string[::-1], 2)
        return b_int

        