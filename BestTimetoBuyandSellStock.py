def maxProfit(prices: list[int]) -> int:
    if not prices: # if list empty return 0
        return 0

    minPrice = prices[0] # (our buy) to start the comparison start at the first element 
    maxProfit = 0 # (diffrence of sell and our buy) initialize max profit at 0 to start with

    for price in prices: # loop over all elements(price) in list(prices)
        if price < minPrice: # if the current element is less that our min price "witch is prices[0] to start"
            minPrice = price # change min price to be current element as we want to buy at the lowest price
        else:
            maxProfit = max(maxProfit, price - minPrice) # if our current element is larger than minprice the, take the max of (previous max price, current max price) to choose the max value possible 
            # note this is like saying let the current element be the maxprofit but the max is there as we need to compare it to the prevous max profit in order to maximize profit
        
    return maxProfit 

print(maxProfit([7, 1, 5, 3, 6, 4])) # returns 5 EX1
print(maxProfit([7, 6, 5, 4, 3, 1])) # returns 0

# Ex 1
# prices[0] = 7
# price is 7, 7 is not < 7 so else runs
# max profit is max of (maxProfit =0, price = 7 - minPrice = 7) which is 0 our Maxprofit is still 0.
# now price is 1, 1 is < 7 so if runs
# minPrice = price(1) so minPrice = 1
# now price is 5 , 5 > 1 so else runs
# maxProfit is max of (0, 5 - 1) max(0, 4) = 4 our maxProfit is now 4
# 3 > 1(minPrice) so else runs and takes max of (4(last maxprofit), 3-1) max(4, 2) = 4 maxProfit still 4
# 6 > 1 else runs
# this time else runs and maxprofit = max(4, 6-1) max(4, 5) = 5 new maxprofit is 5 
# 4 > 1 else runs
# maxprofit = max(5, 4-1) maxProfit is still 5
# LOOP ENDS
# our max profit is 5 from buying at 1(minPrice) and selling at 5(maxProfit)
# return max profit and stop!