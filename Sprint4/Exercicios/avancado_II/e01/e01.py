with open('number.txt') as file:
    dados = file.readlines()

lista_numeros = list(map(
    lambda num: -int(num.replace('-', '')) if '-' in num else int(num),
    dados
))

lista_numeros_pares = list(filter(
    lambda num: num % 2 == 0,
    lista_numeros
))

lista_ordem_decrescente = sorted(lista_numeros_pares, reverse=True)
maiores_numeros = lista_ordem_decrescente[:5]

print(maiores_numeros)
print(sum(maiores_numeros))
