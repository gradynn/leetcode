class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_water = min(height[l], height[r]) * (r - l)

        while l < r:
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
            new_water = min(height[l], height[r]) * (r - l)
            max_water = max(max_water, new_water)

        return max_water