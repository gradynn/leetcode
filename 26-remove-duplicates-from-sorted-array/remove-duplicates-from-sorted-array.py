class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w, r = 0, 0
        while r < len(nums):
            nums[w] = nums[r]
            while r < len(nums) and nums[r] == nums[w]:
                r += 1
            w += 1

        return w