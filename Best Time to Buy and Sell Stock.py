# Solution : 1

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        maxSale = prices[len(prices)-1]
        for i in range(len(prices)-2,-1,-1):
            if maxSale - prices[i] >  maxProfit:
                maxProfit = maxSale - prices[i]
            elif prices[i]>maxSale:
                maxSale = prices[i]
        return maxProfit
      
# Solution : 2 [Kadane's algorithm (DP)]
# Remember the past computation result and update value only if the current value contirbutes positively towards what we want to achieve.
  
  
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maxProfit = 0
        while sell<len(prices):
          currProfit = prices[sell] - prices[buy]
          if prices[buy]<prices[sell]:
            maxProfit = max(maxProfit,currProfit)
          else:
            buy = sell
          sell += 1
        return maxProfit
    
