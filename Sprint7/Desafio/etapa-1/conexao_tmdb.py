import requests, json
import boto3
from datetime import datetime

API_KEY = ""


def solicitacao_tmdb() -> str:
    """
    Efetua uma requisisação para informações presentes no TMDb.

    :return: Informações do TMDb.
    :rtype: str
    """
    url = f"https://api.themoviedb.org/3/genre/movie/list?language=en"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.get(url, headers=headers)
    return response.text

def criar_arquivo_json(data:str) -> None:
    """
    Cria um arquivo JSON no atual diretório e escreve nele o conteúdo retornado pela função solicitacao_tmdb()

    :param data: Conteúdo arquivo gerado.
    :type data: dict
    """
    with open("dados_tmdb.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def enviar_para_nuvem() -> None:
    """
    Envia o arquivo JSON para um bucket no S3.
    """
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('projeto-tmdb')
    data_atual = datetime.now().strftime("%Y/%m/%d")
    bucket.upload_file('dados_tmdb.json', f'Raw/TMDB/JSON/{data_atual}/dados_tmdb.json')


if __name__ == "__main__":
    data = json.loads(solicitacao_tmdb())
    criar_arquivo_json(data)
    enviar_para_nuvem()
