class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1 for i in range(len(ratings))]
        
        # forwards pass
        l, r = 0, 1
        while r < len(ratings):
            if ratings[l] < ratings[r]:
                candies[r] = candies[l] + 1
            l, r = l + 1, r + 1
        
        # backwards pass
        l, r = len(ratings) - 2, len(ratings) - 1
        while l >= 0:
            if ratings[l] > ratings[r]:
                candies[l] = max(candies[r] + 1, candies[l])
            l, r = l - 1, r - 1
        
        print(candies)
        return sum(candies)