# -*- Encoding:UTF-8 -*-

# 714. Best Time to Buy and Sell Stock with Transaction Fee

# Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i;
# and a non-negative integer fee representing a transaction fee.
#
# You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
# You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)
#
# Return the maximum profit you can make.
#
# Example 1:
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# Buying at prices[0] = 1
# Selling at prices[3] = 8
# Buying at prices[4] = 4
# Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
#
# Note:
# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.


class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # DP
        '''
        ans = 0
        hold = -prices[0]
        i = 1
        while i < len(prices):
            ans = max(ans, hold+prices[i]-fee)
            hold = max(hold, ans-prices[i])
            i += 1
        return ans
        '''
        # Greedy
        profit = 0
        curProfit = 0
        minP = prices[0]
        maxP = prices[0]
        i = 1
        while i < len(prices):
            minP = min(minP, prices[i])
            maxP = max(maxP, prices[i])
            curProfit = max(curProfit, prices[i]-minP-fee)
            if maxP-prices[i] >= fee:
                profit += curProfit
                curProfit = 0
                minP = prices[i]
                maxP = prices[i]
            i += 1
        return profit + curProfit


