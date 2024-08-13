class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if prerequisites == []:
            return range(numCourses)

        adj_list = { c:[] for c in range(numCourses)}
        for c, p in prerequisites:
            adj_list[c].append(p)
        
        out = []
        seen, cycle = set(), set()
        def dfs(c):
            if c in cycle:
                return False
            if c in seen:
                return True

            cycle.add(c)
            for pr in adj_list[c]:
                if not dfs(pr):
                    return False

            cycle.remove(c)
            seen.add(c)
            out.append(c)
            return True

        for i in range(numCourses):    
            if not dfs(i):
                return []
        return out