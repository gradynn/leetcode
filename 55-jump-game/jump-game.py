class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jl = [0]
        for i in range(1, len(nums)):
            max_left = max(jl[i - 1] - 1, nums[i - 1] - 1)
            if max_left < 0:
                return False
            jl.append(max_left)
        return True
            