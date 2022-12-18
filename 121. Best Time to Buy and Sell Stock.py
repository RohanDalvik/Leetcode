class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1 #left is buy and right is selling
        maxP=0
        profit=0
        while (r<len(prices)):
            #profitable?
            if prices[l]<prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP,profit)
            else:
                l=r
            r+=1
        return maxP