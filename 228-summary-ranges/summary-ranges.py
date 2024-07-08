class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        out = []

        i = 0
        while i < len(nums):
            start = i
            while i < len(nums) - 1 and nums[i + 1] == nums[i] + 1:
                i += 1
            if start == i:
                out.append(str(nums[i]))
            else:
                out.append(f'{nums[start]}->{nums[i]}')
            i += 1
    
        return out

        