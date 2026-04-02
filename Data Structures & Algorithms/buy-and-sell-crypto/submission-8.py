class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0

        left, right = 0, 1
        while left < right and right < len(prices):
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)

            if prices[right] < prices[left]:
                left = right 
            right += 1

        return max_profit 







# return the max profit can be made 
## meaning that we want to buy in the lowest price and sell at the highest price
## what do we need:
## a tracker of max_profit 
## two pointers -> left, right 
## what is the flow? 
    ## cal the area 
    ## update the max 
    ## move the pointer 
    ### left should be to the right 
    ### right += 1



# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        

#         max_profit = 0 
#         for i in range(len(prices)):
#             for j in range(i + 1, len(prices)):
#                 profit= prices[j] - prices[i]
#                 max_profit = max(max_profit, profit)

#         return max_profit 


