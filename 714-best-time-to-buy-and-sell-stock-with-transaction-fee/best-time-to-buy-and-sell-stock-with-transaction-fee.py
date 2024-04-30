class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        holding = [-(prices[0] + fee)]
        notHolding = [0]

        for i in range(1, len(prices)):
            # holding at the end of ith day
            holding.append(max(
                holding[i - 1], # we are still holding
                -(prices[i] + fee) + notHolding[i - 1] # we have bought
            ))

            # not holding at the end of ith day
            notHolding.append(max(
                holding[i - 1] + prices[i], # we have sold
                notHolding[i - 1], # we are still waiting to buy
            ))
        
        return max(holding[len(prices) - 1], notHolding[len(prices) - 1])