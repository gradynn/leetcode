class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[0])
        print(points)
        
        endOfGroup = points[0][1]
        arrowsShot = 1
        for start, end in points[1:]:
            if start > endOfGroup:
                arrowsShot += 1
                endOfGroup = end
            else:
                endOfGroup = min(end, endOfGroup)
        return arrowsShot