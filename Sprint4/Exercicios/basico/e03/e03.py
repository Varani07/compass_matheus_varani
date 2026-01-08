def mesclar_info(nomes:list, sobrenomes:list, idades:list):
    valores = list(zip(nomes, sobrenomes, idades))

    for i, info in enumerate(valores):
        print(f"{i} - {info[0]} {info[1]} está com {info[2]} anos")

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

mesclar_info(nomes=primeirosNomes, sobrenomes=sobreNomes, idades=idades)