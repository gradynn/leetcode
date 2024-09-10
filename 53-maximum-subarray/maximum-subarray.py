class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')

        running_sum, prefix_sum = 0, 0
        for i in range(len(nums)):
            running_sum += nums[i]
            if prefix_sum < 0:
                running_sum -= prefix_sum
                prefix_sum = 0
            max_sum = max(running_sum, max_sum)
            prefix_sum += nums[i]

        return int(max_sum)