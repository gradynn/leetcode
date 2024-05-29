class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # build pref, suff
        pref = [1]
        suf = [1]
        for i in range(1, len(nums)):
            pref.append(pref[i - 1] * nums[i - 1])
            suf.append(suf[i - 1] * nums[-i])
        suf = suf[::-1]

        # build out
        return [pref[i] * suf[i] for i in range(len(pref))]
