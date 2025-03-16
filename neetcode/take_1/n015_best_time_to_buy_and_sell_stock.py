from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        elif len(prices) == 2:
            return max(prices[1] - prices[0], 0)

        min_so_far = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price > min_so_far:
                max_profit = max(max_profit, price - min_so_far)
            elif price < min_so_far:
                min_so_far = price

        return max_profit


if __name__ == "__main__":
    s = Solution()
    # prices = [10, 1, 5, 6, 7, 1]
    prices = [10, 8, 7, 5, 2]
    result = s.maxProfit(prices=prices)
    print(result)
