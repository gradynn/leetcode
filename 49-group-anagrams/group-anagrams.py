class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            enc = [0] * 26

            for c in s:
                enc[ord(c) - ord('a')] += 1
            
            groups[tuple(enc)].append(s)
        
        return list(groups.values())