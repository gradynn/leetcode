class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda a: a[0])
        out = []
        
        i = 0
        while i < len(intervals):
            start, end = intervals[i][0], intervals[i][1]
            while i < len(intervals) - 1 and intervals[i + 1][0] <= end:
                i += 1
                end = max(intervals[i][1], end)
            out.append([start, end])
            i += 1
        
        return out