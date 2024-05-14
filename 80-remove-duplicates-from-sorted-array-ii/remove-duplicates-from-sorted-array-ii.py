class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        count = 0
        while r < len(nums):
            if nums[r] != nums[r - 1]:
                count = 0

            if count < 2:
                nums[l] = nums[r]
                count += 1
                l += 1
            r += 1
        return l


            
