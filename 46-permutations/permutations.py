class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        out = []

        def dfs(path: List[int]):
            if (len(path) == n):
                out.append(path)
                return
            
            for i in nums:
                if i not in path:
                    dfs(path + [i])
        dfs([])

        return out
