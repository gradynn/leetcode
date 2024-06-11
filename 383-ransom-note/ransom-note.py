class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = defaultdict(int)
        
        for c in magazine:
            hashmap[c] += 1
        
        for c in ransomNote:
            if hashmap[c] == 0:
                return False
            hashmap[c] -= 1
        
        return True