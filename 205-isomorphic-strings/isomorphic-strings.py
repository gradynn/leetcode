class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = defaultdict(lambda: None)
        map_t = defaultdict(lambda: None)

        for i in range(len(s)):
            if not map_s[s[i]] and not map_t[t[i]]:
                map_s[s[i]] = t[i]
                map_t[t[i]] = s[i]
                continue
            
            if map_s[s[i]] != t[i] or map_t[t[i]] != s[i]:
                return False
        
        return True
            
