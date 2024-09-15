class Solution:
    def __init__(self, lista: list[chr]) -> None:
        self.lista = lista

    def reverseString(self) -> list:
        # return self.lista.reverse
        new_list =[]
        if not self.lista:
            return new_list
        for i in range(0, len(self.lista)):
            new_list.append(self.lista[len(self.lista)-i-1])
        return new_list
    
test_solution = Solution(lista=["H","a","n","n","a","h"])
result= test_solution.reverseString()
print (result)

