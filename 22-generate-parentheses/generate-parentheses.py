class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []

        def dfs(path, oCount, cCount):
            if oCount == n and cCount == n:
                out.append(path)
            
            if oCount < n:
                dfs(path + "(", oCount + 1, cCount)
            if cCount < oCount:
                dfs(path + ")", oCount, cCount + 1)
        dfs("(", 1, 0)

        return out