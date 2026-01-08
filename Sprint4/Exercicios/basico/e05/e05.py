import json

with open('person.json') as file:
    dados = json.load(file)

print(dados)