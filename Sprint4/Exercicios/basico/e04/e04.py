def retirar_repetidos(lista:list) -> list:
    return list(set(lista))

a = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
print(retirar_repetidos(a))