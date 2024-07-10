class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        print(points)
        
        i, count = 0, 0
        end = 0
        while i < len(points):
            end = points[i][1]
            while i + 1 < len(points) and points[i + 1][0] <= end:
                end = min(end, points[i + 1][1])
                i += 1
            count += 1
            i += 1
        
        return count
