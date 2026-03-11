import boto3
import zipfile
from pathlib import Path
from datetime import datetime


def extrair() -> None:
    """
    Extrai os arquivos presentes no atual diretório.
    """
    for file in Path(".").glob("*.zip"):
        with zipfile.ZipFile(file, "r") as zip_ref:
            print("Extraindo arquivos...")
            zip_ref.extractall()
            print(f"{file.name} descompactado!")

def enviar_para_nuvem() -> None:
    """
    Envia os arquivos CSV para um bucket no S3.
    """
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('projeto-tmdb')
    data_atual = datetime.now().strftime("%Y/%m/%d")
    for item in ['Movies', 'Series']:
        bucket.upload_file(f'{item.lower()}.csv', f'Raw/Local/CSV/{item}/{data_atual}/{item.lower()}.csv')


if __name__ == "__main__":
    extrair()
    enviar_para_nuvem()
