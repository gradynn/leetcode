class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for num in nums:
            if num not in nums[:k]:
                nums[k] = num
                k += 1
        return k