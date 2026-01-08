from typing import Callable

def my_map(lista:list, f: Callable[[int], int]) -> list:
    nova_lista = [f(item) for item in lista]
    return nova_lista

print(my_map([1,2,3,4,5,6,7,8,9,10], lambda num: num ** 2))