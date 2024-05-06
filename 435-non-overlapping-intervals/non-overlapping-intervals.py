class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[0])
        
        minToRemove = 0
        i = 0
        while i + 1 < len(intervals):
            if intervals[i + 1][0] < intervals[i][1]:
                if intervals[i + 1][1] > intervals[i][1]:
                    intervals.pop(i + 1)
                    minToRemove += 1
                else:
                    intervals.pop(i)
                    minToRemove += 1
            else:
                i += 1
        
        return minToRemove
