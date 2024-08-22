class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []

        def dfs(path, m):
            if sum(path) > target or m >= len(candidates):
                return
            elif sum(path) == target:
                out.append(path)
                return
            
            # include the min
            dfs(path + [candidates[m]], m)
            # don't include the min
            dfs(path, m + 1)
        dfs([], 0)

        return out

        