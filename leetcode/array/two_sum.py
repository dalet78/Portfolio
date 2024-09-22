import itertools

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        permutazioni = self.permutazioni(nums)
        for comb in permutazioni:
            if sum([nums[i] for i in comb]) == target:
                print(f'Combinazione di indici: {comb}, Somma: {[nums[i] for i in comb]}')
                return comb
        return -1
        

    def permutazioni (self, lista) ->list:
        result = []
        for r in range(1, len(lista)+1):
            result.extend([list(comb) for comb in itertools.combinations(range(len(lista)),r)])
        return result

lista = [3,3]
solution =  Solution()
result = solution.twoSum(lista, target= 6)
# print(result)