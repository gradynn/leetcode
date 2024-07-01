class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1:
            return False
        
        in_play = defaultdict(lambda: 0)
        
        l = 0
        r = l + k

        for i in range(l, min(r + 1, len(nums))):
            if in_play[nums[i]] == 1:
                return True
            else:
                in_play[nums[i]] += 1
        
        while r < len(nums) - 1:
            in_play[nums[l]] -= 1
            
            l, r = l + 1, r + 1

            if in_play[nums[r]] == 1:
                return True
            else:
                in_play[nums[r]] += 1

        return False