class Solution:
    def isPalindrome(self, x: int) -> bool:
        f = str(x)
        b = str(x)[::-1]
        return f == b