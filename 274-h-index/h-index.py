class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        
        for i, h in enumerate(citations):
            if n - i <= h:
                return n - i

        return 0