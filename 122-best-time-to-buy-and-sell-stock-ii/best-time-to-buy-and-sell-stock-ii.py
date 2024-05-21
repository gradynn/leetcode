class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        h = [-prices[0]]
        nh = [0]
        for i in range(1, len(prices)):
            h.append(max(
                nh[i - 1] - prices[i],
                h[i - 1]
            ))
            nh.append(max(
                h[i  - 1] + prices[i],
                nh[i - 1]
            ))
        return nh[-1]
        