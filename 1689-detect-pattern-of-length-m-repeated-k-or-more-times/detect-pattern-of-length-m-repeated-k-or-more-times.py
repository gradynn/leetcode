'''
    Sliding Window.
'''

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m):
            pattern = arr[i:i+m]
            count = 1
            s, e = i + m, i + (2 * m)
            while arr[s:e] == pattern:
                count += 1
                if count == k:
                    return True
                s, e = s + m, e + m
        return False
