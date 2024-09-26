class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mh = []
        heapq.heapify(mh)

        for num in nums:
            heapq.heappush(mh, num)

            while len(mh) > k:
                heapq.heappop(mh)
        
        return heapq.heappop(mh)
