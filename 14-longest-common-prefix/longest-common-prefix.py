class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lens = [len(s) for s in strs]
        n = min(lens)
        lp = ""
        for i in range(0, n):
            c = strs[0][i]
            for str in strs[1:]:
                if str[i] != c:
                    return lp
            lp += c
        return lp