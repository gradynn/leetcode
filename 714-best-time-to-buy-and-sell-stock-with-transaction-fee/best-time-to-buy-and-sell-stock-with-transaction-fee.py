class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        holding = -(prices[0] + fee)
        notHolding = 0

        for i in range(1, len(prices)):
            holding, notHolding = max( # holding at end of ith day
                holding, # we are still holding
                -(prices[i] + fee) + notHolding # we have bought
            ), max( # not holding at end of ith day
                holding + prices[i], # we have sold
                notHolding # we are still waiting to buy
            )
        
        return max(holding, notHolding)