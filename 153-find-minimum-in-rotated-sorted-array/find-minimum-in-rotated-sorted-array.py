class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        out = float('inf')
        while l <= r:
            m = (l + r) // 2

            out = min(nums[m], out)

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        
        return int(out)
