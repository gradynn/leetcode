class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]
        locMax, locMin = 0, 0
        total = 0

        for n in nums:
            locMax = max(locMax + n, n)
            locMin = min(locMin + n, n)
            total += n
            globMax = max(locMax, globMax)
            globMin = min(locMin, globMin)
        
        if globMax > 0:
            return max(globMax, total - globMin)
        else:
            return globMax