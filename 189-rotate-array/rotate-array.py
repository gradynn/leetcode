class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_cpy = [0] * len(nums)
        for i in range(len(nums)):
            new_index = (i + k) % len(nums)
            nums_cpy[new_index] = nums[i]

        for i in range(len(nums)):
            nums[i] = nums_cpy[i]
