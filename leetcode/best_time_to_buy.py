class Solution:
    def __init__(self, prices: list[int]) -> None:
        self.prices = prices

    def maxProfit(self) -> int:
        total_profit=0
        temp_profit_list = [0,0]
        for i in range(0, len(self.prices)-1):
            for j in range (i, len(self.prices)-i):
                if self.prices[j+1] >= self.prices[j]:
                    pass
        return self.prices 
    

test_solution = Solution(nums=[0,0,1,1,1,2,2,3,3,4])
result= test_solution.removeDuplicates()
print (result)