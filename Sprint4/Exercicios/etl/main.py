from typing import TypedDict
from pathlib import Path


class DadosAtores(TypedDict):
    atores: tuple[str, ...]
    receita_bruta_total: tuple[float, ...]
    numero_filmes: tuple[int, ...]
    media_por_filme: tuple[float, ...]
    filme_num_1: tuple[str, ...]
    receita_bruta: tuple[float, ...]


def read_file(arquivo:str) -> list[str]:
    """
    Lê o arquivo especificado.

    Args:
        arquivo (str): Nome do arquivo a ser lido junto com sua extensão.

    Returns:
        list[str]: Linhas do arquivo.

    Examples:
        >>> read_file('hello.txt')
        ['Coding in python.\\n', 'Hello World!\\n']
    """

    with open(arquivo, encoding='utf-8') as file:
        dados = file.readlines()
        
    return dados


def write_file(nome_arquivo:str, conteudo:str) -> None:
    """
    Escreve o conteúdo em um arquivo.

    Args:
        nome_arquivo (str): Nome do arquivo com sua extensão.
        conteudo (str): O que será escrito no arquivo.
    """

    with open(nome_arquivo, 'w', encoding='utf-8') as file:
        file.write(conteudo)


def organizar_dados(lista:list[str]) -> DadosAtores:
    """
    Organiza as informações do arquivo actors.csv.

    Args:
        lista (list[str]): Linhas do arquivo actors.csv.

    Returns:
        DadosAtores: Informações estruturadas, formatadas e prontas para uso.
    """

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
    # Actor,Total Gross,Number of Movies,Average per Movie,#1 Movie,Gross
    dicionario = {
        'atores': informacoes_organizadas[0],
        'receita_bruta_total': tuple([float(valor) for valor in informacoes_organizadas[1]]),
        'numero_filmes': tuple([int(valor) for valor in informacoes_organizadas[2]]),
        'media_por_filme': tuple([float(valor) for valor in informacoes_organizadas[3]]),
        'filme_num_1': informacoes_organizadas[4],
        'receita_bruta': tuple([float(valor) for valor in informacoes_organizadas[5]])
    }
    return dicionario


def etapa_1(atores:tuple[str, ...], numero_filmes:tuple[int, ...]) -> None:
    """
    Escreve no arquivo 'etapa-1.txt' quem é o ator/atriz com o maior número de filmes e a quantidade.

    Args:
        atores (tuple[str, ...]): Atores/Atrizes.
        numero_filmes (tuple[int, ...]): Número de filmes de cada ator/atriz.
    """

    maior_num_filmes = max(numero_filmes)
    id_ator = numero_filmes.index(maior_num_filmes)
    nome_ator = atores[id_ator]

    write_file('etapa-1.txt', f"O ator/atriz com maior número de filmes é {nome_ator}, com respectivamente {maior_num_filmes} filmes.")


def etapa_2(receita_bruta:tuple[float, ...]) -> None:
    """
    No arquivo 'etapa-2.txt', apresenta a média da receita de bilheteria bruta dos principais filmes, levando em conta todos atores/atrizes.

    Args:
        receita_bruta (tuple[float, ...]): Receita bruta dos principais filmes de cada ator/atriz.
    """

    media_receita = sum(receita_bruta)/len(receita_bruta)
    write_file('etapa-2.txt', f"Considerando todos os atores, a média da receita bruta de seus principais filmes é de US${media_receita} milhões.")


def etapa_3(media_por_filme:tuple[float, ...], atores:tuple[str, ...]) -> None:
    """
    Escreve no arquivo 'etapa-3.txt' qual ator/atriz possui a maior média de bilheteria bruta por filme em conjunto com o valor respectivo.

    Args:
        media_por_filme (tuple[float, ...]): Média de bilheteria bruta por filme dos atores/atrizes.
        atores (tuple[str, ...]): Atores/Atrizes.
    """

    maior_media = max(media_por_filme)
    id_ator = media_por_filme.index(maior_media)
    nome = atores[id_ator]
    write_file(nome_arquivo='etapa-3.txt', conteudo=f'O ator/atriz com a maior média de receita de bilheteria bruta por filme é {nome}, tendo respectivamente US${maior_media} milhões.')


def etapa_4(filme_num_1:tuple[str, ...]) -> None:
    """
    Popula o arquivo 'etapa-4.txt' com os filmes do dataset em ordem decrescente por quantas vezes aparecem e nome.

    Args:
        filme_num_1 (tuple[str, ...]): Filmes de maior bilheteria em que os atores/atrizes atuaram. 
    """

    conteudo = ''

    contagem_filmes = {filme: filme_num_1.count(filme) for filme in set(filme_num_1)}
    filmes_ordenados = sorted(
        contagem_filmes.items(), 
        key=lambda valores: (-valores[1], valores[0])
    )
    
    for i, filme in enumerate(filmes_ordenados, 1):
        conteudo += f"{i} - O filme {filme[0]} aparece {filme[1]} vez(es) no dataset.\n"

    write_file('etapa-4.txt', conteudo)


def etapa_5(atores:tuple[str, ...], receita_bruta_total:tuple[float, ...]) -> None:
    """
    Apresenta, no arquivo 'etapa-5.txt', uma lista dos atores ordenada pela receita bruta total em ordem decrescente.

    Args:
        atores (tuple[str, ...]): Atores/Atrizes.
        receita_bruta_total (tuple[float, ...]): Receita bruta de bilheteria dos filmes de cada ator.
    """

    listas_mescladas = list(zip(atores, receita_bruta_total))
    lista_ordenada = sorted(listas_mescladas, key=lambda item: item[1], reverse=True)
    conteudo = "".join(
        f"{item[0]} - {item[1]}\n"
        for item in lista_ordenada
    )
    write_file('etapa-5.txt', conteudo)


def comparar_arquivos() -> dict[str, dict[str, list[str]]]:
    """
    Compara os arquivos 'etapa-4.txt' e 'etapa-5.txt' com os arquivos presentes nas pastas da pasta 'etl_colegas'.

    Returns:
        dict[str, dict[str, list[str]]]: Diferenças encontradas em cada arquivo.
    """

    diferencas = {}

    etapa_4 = read_file('etapa-4.txt')
    etapa_5 = read_file('etapa-5.txt')

    execicio_colegas = Path('etl_colegas')
    for pasta in execicio_colegas.iterdir():
        if not pasta.is_dir():
            continue

        for arquivo in pasta.iterdir():
            if not arquivo.is_file():
                continue

            linhas = read_file(str(arquivo))
            for linha in zip(etapa_4 if '4' in arquivo.name else etapa_5, linhas):
                if linha[0] != linha[1]:
                    if pasta.name not in diferencas:
                        diferencas[pasta.name] = {}
                    
                    if arquivo.name not in diferencas[pasta.name]:
                        diferencas[pasta.name][arquivo.name] = []
                    diferencas[pasta.name][arquivo.name].append(f'meu: "{linha[0]}" != colega: "{linha[1]}"')
    return diferencas


def realizar_etapas() -> None:
    dados = organizar_dados(read_file('actors.csv'))

    etapa_1(atores=dados['atores'], numero_filmes=dados['numero_filmes'])
    etapa_2(receita_bruta=dados['receita_bruta'])
    etapa_3(media_por_filme=dados['media_por_filme'], atores=dados['atores'])
    etapa_4(filme_num_1=dados['filme_num_1'])
    etapa_5(atores=dados['atores'], receita_bruta_total=dados['receita_bruta_total'])

    # for colega, etapas in comparar_arquivos().items():
    #     if colega in ['']:
    #         print(f"{colega}:")
    #         for etapa, diffs in etapas.items():
    #             print(f"{etapa}:")
    #             print(diffs)

                # for diff in diffs:
                #     print(diff)

    for i in range(1, 6):
        if i not in [4, 5]:
            print(read_file(f'etapa-{i}.txt')[0])
        else:
            for linha in read_file(f'etapa-{i}.txt'):
                print(linha, end="")


if __name__ == '__main__':
    realizar_etapas()