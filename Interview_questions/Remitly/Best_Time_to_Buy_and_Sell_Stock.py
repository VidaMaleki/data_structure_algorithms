"""121. Best Time to Buy and Sell Stock
Solved
Easy
Topics
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Initialize with a very high value
        max_profit = 0  # Track the maximum profit
        
        for price in prices:
            if price < min_price:
                min_price = price  # Update minimum buying price
            else:
                max_profit = max(max_profit, price - min_price)  # Update max profit
        
        return max_profit

# Example Test Cases
solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))  # Output: 5
print(solution.maxProfit([7,6,4,3,1]))  # Output: 0


"""Explanation:
For prices = [7,1,5,3,6,4]:

Day 1: min_price = 7, max_profit = 0
Day 2: min_price = 1, max_profit = 0
Day 3: max_profit = 5 - 1 = 4
Day 4: max_profit remains 4
Day 5: max_profit = 6 - 1 = 5
Day 6: max_profit remains 5
✅ Output: 5

For prices = [7,6,4,3,1]:

Prices keep decreasing → No profit can be made.
Output: 0
Time Complexity:O(N) → We traverse the list once.
Space Complexity: O(1) → Only two variables used."""