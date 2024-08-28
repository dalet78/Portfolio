class Solution:
    def __init__(self, nums: list[int]) -> None:
        self.nums = nums

    def remove_duplicate(self):
        list_without_duplicate =[]
        for elem in self.nums:
            if elem not in list_without_duplicate:
                list_without_duplicate.append(elem)
        return list_without_duplicate
    
    def list_order(self):
        self.nums = sorted(self.nums)

    def removeDuplicates(self) -> int:
        list_without_duplicate = self.remove_duplicate()
        k= len(list_without_duplicate)
        self.nums =  list_without_duplicate
        return (self.nums, k) 
    

test_solution = Solution(nums=[0,0,1,1,1,2,2,3,3,4])
result= test_solution.removeDuplicates()
print (result)