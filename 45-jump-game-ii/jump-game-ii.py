class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        l = r = 0
        while r != len(nums) - 1:
            furthest = -1

            for i in range(l, r + 1):
                furthest = max(furthest, min(i + nums[i], len(nums) - 1))
            
            if furthest > r:
                l = l + 1
                r = furthest
                count += 1
        
        return count
