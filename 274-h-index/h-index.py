class Solution:
    def hIndex(self, citations: List[int]) -> int:
        bound = max(citations)
        h_index = 0
        
        for h in range(1, bound + 1):
            if len(list(filter(lambda x : x >= h, citations))) >= h:
                h_index = h
            else:
                break

        return h_index