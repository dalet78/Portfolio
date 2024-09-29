def print_items(n: int) -> int:
    lista = list(range(0,n))
    print(*[str(x) for x in lista], sep='\n')

# def print_items(n):
#     for i in range(n):
#         print(i)

print_items(10)