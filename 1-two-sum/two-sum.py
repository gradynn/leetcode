class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = defaultdict(lambda: -1)
        for i in range(len(nums)):
            comp = target - nums[i]
            if pairs[nums[i]] != -1:
                return [i, pairs[nums[i]]]
            else:
                pairs[comp] = i
            