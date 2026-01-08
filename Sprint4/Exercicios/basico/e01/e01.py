a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def lista_num_impar(lista: list):
    numeros_impares = [num for num in lista if num % 2 != 0]
    return numeros_impares
    
print(lista_num_impar(a))