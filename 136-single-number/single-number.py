class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mask = nums[0]
        for i in range(1, len(nums)):
            mask = mask ^ nums[i]
        return mask