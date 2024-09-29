class Solution:
    def romanToInt(self, s: str) -> int:
        string_list = self.divide_string_chart_to_list(s)
        return self.convert_to_integer(string_list)

    def divide_string_chart_to_list(self, str) -> list:
        list_char = []
        for char in str:
            list_char.append(char)
        return list_char
    
    def convert_value_in_number(self, string_list):
        new_list = []
        for i in string_list:
            if i == 'M':
                new_list.append(1000)
            elif i == 'D':
                new_list.append(500)
            elif i == 'C':
                new_list.append(100)
            elif i == 'L':
                new_list.append(50)
            elif i == 'X':
                new_list.append(10)
            elif i == 'V':
                new_list.append(5)
            else:
                new_list.append(1)
        return new_list
    
    def convert_to_integer(self, string_list) -> int:
        new_list = self.convert_value_in_number(string_list)
        result = 0
        i = 0  # Inizializziamo l'indice i

        while i < len(new_list):
            if i < len(new_list) - 1:  # Assicurati che i+1 non vada fuori dall'indice
                if new_list[i] == 100 and new_list[i + 1] == 1000:
                    result += 900
                    i += 2  # Saltiamo 2 posizioni
                elif new_list[i] == 100 and new_list[i + 1] == 500:
                    result += 400
                    i += 2
                elif new_list[i] == 10 and new_list[i + 1] == 100:
                    result += 90
                    i += 2
                elif new_list[i] == 10 and new_list[i + 1] == 50:
                    result += 40
                    i += 2
                elif new_list[i] == 1 and new_list[i + 1] == 10:
                    result += 9
                    i += 2
                elif new_list[i] == 1 and new_list[i + 1] == 5:
                    result += 4
                    i += 2
                else:
                    result += new_list[i]
                    i += 1
            else:
                result += new_list[i]
                i += 1
            
        return result


stringa = "MCMXCIV"
solution =  Solution()
result = solution.romanToInt(stringa)
print(result)