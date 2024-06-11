class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l = 0
        max_substring = 0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            max_substring = max(max_substring, r - l + 1)
        return max_substring