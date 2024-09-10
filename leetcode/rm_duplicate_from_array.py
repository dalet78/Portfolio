class Solution:
    def __init__(self, nums: list[int]) -> None:
        self.nums = nums

    def removeDuplicates(self) -> int:
        if not self.nums:
            return 0

        # Initialize the index for unique elements
        k = 1

        # Go through the sorted array and remove duplicates in-place
        for i in range(1, len(self.nums)):
            if self.nums[i] != self.nums[i - 1]:  # if current is different from the previous
                self.nums[k] = self.nums[i]  # place it at the next position for unique elements
                k += 1

        return k
    

test_solution = Solution(nums=[0,0,1,1,1,2,2,3,3,4])
result= test_solution.removeDuplicates()
print (result)