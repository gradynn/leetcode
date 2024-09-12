'''
    Run binary search.
    Check if middle is peak
    Discard left if right neighbor of middle is bigger than left
    Discard right if left neighbor of middle is bigger than right
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def isPeak(index: int) -> bool:
            if (index == len(nums) - 1 or nums[index] > nums[index + 1]) and (index == 0 or nums[index] > nums[index - 1]):
                return True
            else:
                return False
        
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if isPeak(m):
                return m
            
            if m == 0:
                l = m + 1
            elif m == len(nums) - 1:
                r = m - 1
            elif nums[m - 1] > nums[m + 1]:
                r = m - 1
            else:
                l = m + 1
        return 0