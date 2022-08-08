class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        lowest= max(prices)
        
        for i in range(len(prices)):
            if prices[i]< lowest:
                lowest = prices[i]
            elif prices[i]- lowest > profit:
                profit= prices[i]- lowest
            
        
        return profit
   
                
                



               
        
            