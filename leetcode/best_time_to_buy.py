class Solution:
    def __init__(self, prices: list[int]) -> None:
        self.prices = prices

    def maxProfit(self) -> int:
        total_profit = 0
        if not self.prices:
            return 0
        
        for i in range(1, len(self.prices)):
            if self.prices[i] > self.prices[i-1]:
                total_profit += self.prices[i]- self.prices[i-1] 
        return total_profit
            

test_solution = Solution(prices=[7,6,4,3,1])
result= test_solution.maxProfit()
print (result)