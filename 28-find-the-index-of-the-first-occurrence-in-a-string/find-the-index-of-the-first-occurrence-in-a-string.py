class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                # search
                j, count = 1, 1
                while i + j < len(haystack) and j < len(needle):
                    if haystack[i + j] != needle[j]:
                        break
                    count += 1
                    j += 1
                if count == len(needle):
                    return i
        return -1