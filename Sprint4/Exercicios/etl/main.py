def read_file(arquivo:str) -> list[str]:
    with open(arquivo, encoding='utf-8') as file:
        dados = file.readlines()
        
    return dados

def write_file(nome_arquivo:str, conteudo:str) -> None:
    with open(nome_arquivo, 'w', encoding='utf-8') as file:
        file.write(conteudo)


def organizar_dados(lista:list[str]) -> list[tuple[str]]:
    del lista[0]
    informacoes = []

    for info in lista:
        if '"' in info:
            info_repartida = info.split(',')
            info_repartida[0] = ",".join([info_repartida[0], info_repartida.pop(1)])
            info_repartida[0] = info_repartida[0].replace('"', "")
            informacoes.append(info_repartida)
            continue
        informacoes.append(info.split(','))
    
    informacoes_organizadas = list(zip(*informacoes))
    return informacoes_organizadas


def etapa_1(dados: list[tuple[str]]):
    numero_de_filmes = [int(num) for num in dados[2]]
    maior_num_filmes = max(numero_de_filmes)
    id_ator = numero_de_filmes.index(maior_num_filmes)
    nome_ator = dados[0][id_ator]

    write_file('etapa-1.txt', f"O ator/atriz com maior número de filmes é {nome_ator}, com respectivamente {maior_num_filmes} filmes.")


def realizar_etapas():
    dados = organizar_dados(read_file('actors.csv'))
    etapa_1(dados)


if __name__ == '__main__':
    realizar_etapas()