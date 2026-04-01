import random, time, os, names


random.seed(40)
qtd_nomes_unicos = 5000
qtd_nomes_aleatorios = 12000

aux = []
for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios...")
dados = []
for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

path = "/home/varani/repos/compass_matheus_varani/Sprint8/Exercicios/ex1/etapa-3/nomes_aleatorios.txt"

os.system(f"[ -f {path} ] || touch {path}")
with open(path, "a") as file:
    [print(nome, file=file) for nome in dados]
