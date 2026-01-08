def dividir_lista(lista:list[int]) -> tuple[list[int], list[int], list[int]]:
    reparticoes = int(len(lista)/3)

    lista1 = []
    lista2 = []
    lista3 = []

    for l in [lista1, lista2, lista3]:
        for _ in range(reparticoes):
            l.append(lista.pop(0))

    return lista1, lista2, lista3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
resultado = dividir_lista(lista)
print(resultado[0], resultado[1], resultado[2])