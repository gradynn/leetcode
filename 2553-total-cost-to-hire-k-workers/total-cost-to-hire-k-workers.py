class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        i = 0
        j = len(costs) - 1
        lHeap = []
        rHeap = []

        cost = 0
        for r in range(k):
            while len(lHeap) < candidates and i <= j:
                heapq.heappush(lHeap, costs[i])
                i += 1
            while len(rHeap) < candidates and i <= j:
                heapq.heappush(rHeap, costs[j])
                j -= 1
            
            v1 = lHeap[0] if lHeap else float('inf')
            v2 = rHeap[0] if rHeap else float('inf')

            if v1 <= v2:
                cost += heapq.heappop(lHeap)
            else:
                cost += heapq.heappop(rHeap)

        return cost