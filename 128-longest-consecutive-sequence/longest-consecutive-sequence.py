class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s_nums = set(nums)
        max_len = 0

        for num in nums:
            if num - 1 not in s_nums:
                count, n = 0, num
                while n in s_nums:
                    count += 1
                    n += 1
                max_len = max(count, max_len)

        return max_len

