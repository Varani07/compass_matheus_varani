with open('arquivo_texto.txt', encoding='utf-8') as file:
    dados = file.readlines()

print("".join(dados), end="")