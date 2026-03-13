import requests, json
import boto3
from datetime import datetime
import time
import os

API_KEY = os.environ.get('TMDB_API_KEY')


def solicitacao_tmdb(info:str) -> dict:
    """
    Efetua uma requisisação para informações presentes no TMDb.

    :param info: Informação que será solicitada.
    :type info: str
    :return: Informações do TMDb.
    :rtype: dict
    """
    url = f"https://api.themoviedb.org/3/{info}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.get(url, headers=headers)
    time.sleep(0.5)
    return json.loads(response.text)

def tratar_dados(search:str, tipo:str) -> list[dict]:
    """
    Organiza as informações recebidas, mantendo apenas colunas e informações necessárias.

    :param search: Pesquisa que será feita.
    :type search: str
    :param tipo: Tipo de dado.
    :type tipo: str
    :return: Informação do TMDb pronta para ser salva em um arquivo.
    :rtype: list[dict]
    """
    genre_ids = [16, 35]
    conteudo_final = []
    match tipo:
        case 'series':
            solicitacao = 'tv'
            delete_keys = ['adult', 'backdrop_path', 'overview', 'poster_path', 'origin_country', 'original_language', 'popularity']
            add_keys = ['last_air_date']
        case _:
            solicitacao = 'movie'
            delete_keys = ['adult', 'backdrop_path', 'overview', 'poster_path', 'popularity', 'video', 'original_language']
            add_keys = ['runtime']
    generos_all = {genre['id']:genre['name'] for genre in solicitacao_tmdb(f'genre/{solicitacao}/list')['genres']}
    for num in range(1, 11):
        data = solicitacao_tmdb(search + f'?page={num}')
        conteudo = data['results']
        for item in conteudo:
            for ids in item['genre_ids']:
                if ids in genre_ids:
                    conteudo_final.append(item)
                    break
        [[item.pop(chave,None) for chave in delete_keys] for item in conteudo_final]
        for item in conteudo_final:
            if any(type(genre_id) == int for genre_id in item['genre_ids']):
                mudancas = []
                for genre_id in item['genre_ids']:
                    mudancas.append((generos_all[genre_id], genre_id))
                for mudanca in mudancas:
                    item['genre_ids'].remove(mudanca[1])
                    item['genre_ids'].append(mudanca[0])
                info_adicional = solicitacao_tmdb(f"{solicitacao}/{str(item['id'])}")
                for novo_item in add_keys:
                    item[novo_item] = info_adicional[novo_item]

    return conteudo_final
            
def enviar_para_nuvem(data:list[dict], tipo:str) -> None:
    """
    Envia os dados JSON para um bucket no S3.

    :param data: Conteúdo que será utilizado para gerar o JSON..
    :type data: list[dict]
    :param tipo: Tipo do arquivo que será gerado no bucket.
    :type tipo: str
    """
    s3 = boto3.client('s3')
    data_atual = datetime.now().strftime("%Y/%m/%d")
    bucket_name = 'projeto-tmdb'
    key = f'Raw/TMDB/JSON/{tipo.capitalize()}/{data_atual}/{tipo}.json'
    
    json_data = json.dumps(data, ensure_ascii=False, indent=4)
    s3.put_object(Bucket=bucket_name, Key=key, Body=json_data.encode('utf-8'), ContentType='application/json')


for requisicao in [('tv/popular','series'), ('movie/popular', 'movies')]:
    data = tratar_dados(requisicao[0], requisicao[1])
    enviar_para_nuvem(data, requisicao[1])
