class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        out = []
        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x - 1]:
                continue

            y = x + 1
            z = len(nums) - 1

            while y < z:
                cur_sum = nums[x] + nums[y] + nums[z]
                if cur_sum == 0:
                    new_set = [nums[x], nums[y], nums[z]]
                    out.append(new_set)
                    y += 1
                    while nums[y] == nums[y - 1] and y < z:
                        y += 1
                elif cur_sum < 0:
                    y += 1
                else:
                    z -= 1
        
        return out