class Solution:
    def counter_character_in_list(self, new_list, character) -> int:
        counter = 0
        for element in new_list:
            if element == character:
                counter +=1
            if counter > 1 :
                return 2
        return counter

    def remove_space_from_list(self, list_char) ->list:
        new_list = []
        for i in list_char:
            if i != " ": 
                new_list.append(i)
        return new_list
    
    def divide_string_chart_to_list(self, str) -> list:
        list_char = []
        for char in str:
            list_char.append(char)
        list_char = self.remove_space_from_list(list_char)
        return list_char

    def firstUniqChar(self, s: str) -> int:
        new_list = self.divide_string_chart_to_list(s)
        for i in range(0, len(new_list)):
            counter = self.counter_character_in_list(new_list, new_list[i])
            if counter == 1:
                return i
        return -1
    

stringa = "abba"
solution =  Solution()
result = solution.firstUniqChar(stringa)
print(result)
    
    
