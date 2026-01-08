with open('estudantes.csv', encoding='utf-8') as file:
    dados = file.readlines()
    dados.sort(key=lambda item: item.split(',')[0])


for dado in dados:
    info = dado.split(',')

    nome_aluno = info[0]
    notas = list(map(
        lambda nota: int(nota),
        info[1:]
    ))

    notas_ordem_decrescente = sorted(notas, reverse=True)[:3]
    media = round(sum(notas_ordem_decrescente)/len(notas_ordem_decrescente), 2)
    
    print(f"Nome: {nome_aluno} Notas: {notas_ordem_decrescente} Média: {media}")
    