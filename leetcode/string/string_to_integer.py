class Solution:
    def myAtoi(self, s: str) -> int:
        new_list = self.transform_string_to_list(s)
        new_list = self.clean_list_from_space(new_list)
        new_list = self.get_only_int_list(new_list)
        if new_list == []:
            return 0
        else:
            return int(''.join(map(str, new_list)))
       
    def transform_string_to_list(self, s)-> list:
        new_list = []
        for char in s:
            new_list.append(char)
        return new_list
    
    def clean_list_from_space(self, lista) -> list:
        return [item for item in lista if item != " "]
    
    def isInteger(self, value) ->bool:
        if value in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            return True
        else:
            return False
    
    def get_only_int_list(self, lista)-> list:
        new_list=[]
        i = 0
        if not (self.isInteger(lista[i]) or lista[i] in ['+', '-']):
            return new_list
        else: 
            new_list.append(lista[i])
            i+=1
        while i < len(lista):
            if not self.isInteger(lista[i]):
                return new_list
            elif lista[i] == "-":
                new_list.append('-')
                i+=1
            else:
                new_list.append(lista[i])
                i+=1

        return new_list
    
stringa = "   -042"
solution =  Solution()
result = solution.myAtoi(stringa)
print(result)
            
            