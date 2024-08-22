class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        def dfs(path):
            if sum(path) > target:
                return
            elif sum(path) == target:
                path.sort()
                if path not in out:
                    out.append(path)
                return

            for i in candidates:
                dfs(path + [i])
        dfs([])

        return out
        