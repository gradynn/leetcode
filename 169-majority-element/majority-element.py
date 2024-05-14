class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            if num not in map.keys():
                map[num] = 1
            else:
                map[num] = map[num] + 1
        
        for num in set(nums):
            if map[num] > len(nums) // 2:
                return num