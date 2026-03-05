import requests, os, json
from dotenv import load_dotenv
import pandas as pd


load_dotenv()
api_key = os.getenv("TMDB_API_KEY")


def info_filmes():
    """
    Acessa The Movie Database e retorna uma lista de generos.
    
    :return: Generos presentes no TMDb.
    :rtype: str
    """

    url = f"https://api.themoviedb.org/3/genre/movie/list?language=en"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers)
    return response.text


if __name__ == "__main__":
    data = json.loads(info_filmes())
    data = data['genres']
    df = pd.DataFrame(data)
    print(df)