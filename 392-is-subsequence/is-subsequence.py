class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr = 0
        for c in t:
            if s_ptr < len(s) and s[s_ptr] == c:
                s_ptr += 1
        return s_ptr == len(s)