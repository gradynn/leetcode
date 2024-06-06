class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ''.join([c.lower() for c in s if c.isalnum()])
        return s_new == s_new[::-1]