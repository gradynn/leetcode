class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []

        def dfs(path: List[int], last: int):
            if len(path) == k:
                out.append(path)
                return
            for i in range(last, n):
                if i + 1 not in path:
                    dfs(path + [i + 1], i + 1)
        dfs([], 0)

        return out
