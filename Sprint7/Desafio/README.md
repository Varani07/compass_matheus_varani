# Desafio
O desafio se dá em duas etapas, na primeira devemos, fazendo uso de um container no docker, executar um python script que vai fazer uso da biblioteca boto3 e enviar dois arquivos CSV para um bucket no Amazon S3.

Na parte 2, fazendo uso do AWS Lambda vamos capturar dados do TMDb para complementar os dados dos filmes e séries.

Esses dados serão utilizados para responder uma série de questões:

1. Relação da duração dos filmes (minutos) e suas respectivas avaliações. | Comédia
    - Tipo:
        - movie
    - Col:
        - tempo_minutos
        - nota_media
    - Genero:
        - Comedy
2. Relação da década em que o filme foi lançado e suas avaliações. | Comédia, Animação
    - Tipo:
        - movie
    - Col:
        - decada
        - nota_media
    - Genero:
        - Comedy
        - Animation
3. Relação do tempo (anos) em que a série ficou no ar e suas avaliações. | Comédia, Animação
    - Tipo:
        - serie
    - Col:
        - ativo
        - nota_media
    - Genero:
        - Comedy
        - Animation
4. Média das notas em cada década. | Animação
    - Tipo:
        - movie
        - serie
    - Col:
        - decada
        - nota_media, AVG
    - Genero:
        - Animation

## Sumário
- [Etapa 1](#etapa-1)
- [Etapa 2](#etapa-2)

## <a name="etapa-1">Etapa 1</a>
 Objetivo: Em um container, rodar um python script que irá subir dois arquivos CSV para um bucket no AWS S3.

- Arquivos:
    - [Dockerfile utilizado para montar o container](/Sprint7/Desafio/etapa-1/Dockerfile)
    - [Python script](/Sprint7/Desafio/etapa-1/carregar_dados.py)
    - [Dependências](/Sprint7/Desafio/etapa-1/requirements.txt)

- Passo a passo:
    - Python script

        ```python
        # importando bibliotecas utilizadas
        import boto3
        import zipfile
        from pathlib import Path
        from datetime import datetime
        from dotenv import load_dotenv


        def extrair() -> None:
            """
            Extrai os arquivos presentes no atual diretório.
            """
            # cria um objeto do diretório atual
            # glob especifica o padrão dos arquivos desejados
            for file in Path(".").glob("*.zip"):
                # abre o arquivo encontrado em modo de leitura
                with zipfile.ZipFile(file, "r") as zip_ref:
                    print("Extraindo arquivos...")
                    # extrai o conteúdo do arquivo
                    zip_ref.extractall()
                    print(f"{file.name} descompactado!")

        def enviar_para_nuvem() -> None:
            """
            Envia os arquivos CSV para um bucket no S3.
            """
            # cria um objeto para referenciar o bucket presente no S3
            s3 = boto3.resource('s3')
            bucket = s3.Bucket('projeto-tmdb')
            # gera a data no formato solicitado
            data_atual = datetime.now().strftime("%Y/%m/%d")
            # itera pelos itens da lista, enviando os arquivos para o S3 de forma dinâmica
            for item in ['Movies', 'Series']:
                bucket.upload_file(f'{item.lower()}.csv', f'Raw/Local/CSV/{item}/{data_atual}/{item.lower()}.csv')


        if __name__ == "__main__":
            # carrega as credênciais inclusas no .env
            load_dotenv()
            # extrai arquivos zip
            extrair()
            # envia os arquivos resultantes ao bucket
            enviar_para_nuvem()
        ```
    - Dockerfile

        ```dockerfile
        # imagem a ser utilizada como base
        FROM condaforge/miniforge3:latest

        # diretório onde o processo irá rodar
        WORKDIR /work

        # copiando todos os arquivos presentes na pasta atual para o WORKDIR
        COPY . .

        # atualiza o pip e instala as dependencias presentes no requirements.txt
        RUN pip install --upgrade pip && \
            pip install -r requirements.txt

        # roda o python script
        CMD ["python", "carregar_dados.py"]
        ```
    - Execução

        ```bash
        # montando imagem
        docker build -t carregar_csv_para_bucket .
        ```
        ![build](/Sprint7/Evidencias/desafio/etapa-1/build.png)
        ```bash
        # subindo container
        docker run --rm carregar_csv_para_bucket
        ```
        ![run](/Sprint7/Evidencias/desafio/etapa-1/run.png)
    - Resultado

        ![series](/Sprint7/Evidencias/desafio/etapa-1/series_bucket.png)
        ![movies](/Sprint7/Evidencias/desafio/etapa-1/movies_bucket.png)

## <a name="etapa-2">Etapa 2</a>
- Objetivo: Capturar dados do TMDb via AWS Lambda e encaminhar ao bucket do desafio.

- Arquivos:
    - [Dockerfile](/Sprint7/Desafio/etapa-2/Dockerfile)
    - [Python script](/Sprint7/Desafio/etapa-2/conexao_tmdb.py)
    - [Bash Script](/Sprint7/Desafio/etapa-2/create_layer)
    - [Camada gerada](/Sprint7/Desafio/etapa-2/minha_camada.zip)

- Passo a passo:
    - Python script

        **Aviso**: Apesar de ter uma função chamada `tratar_dados`, sua funcionalidade se baseia em retirar colunas desnecessárias, filtrar apenas os dados desejados e substituir informações como o id do gênero por seu nome, que é o que de fato será utilizado. Então cumprindo com o propósito de serem informações relevantes para as respostas das perguntas formuladas anteriormente e não indo contra as exigências.
        ```python
        # importando bibliotecas que serão utilizadas
        import requests, json
        import boto3
        from datetime import datetime
        import time
        import os

        # carregando variavel de ambiente
        API_KEY = os.environ.get('TMDB_API_KEY')


        def solicitacao_tmdb(info:str) -> dict:
            """
            Efetua uma requisisação para informações presentes no TMDb.

            :param info: Informação que será solicitada.
            :type info: str
            :return: Informações do TMDb.
            :rtype: dict
            """
            # organizando requisição que será efetuada
            url = f"https://api.themoviedb.org/3/{info}"
            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {API_KEY}"
            }
            response = requests.get(url, headers=headers)
            # definindo delay para não fazer muitas requisições por segundo
            time.sleep(0.5)
            # retornando um dicionário contendo a resposa da requisição
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
            # definindo generos que serão utilizados
            genre_ids = [16, 35]
            conteudo_final = []
            # definindo informações dinâmicas
            match tipo:
                case 'series':
                    solicitacao = 'tv'
                    delete_keys = ['adult', 'backdrop_path', 'overview', 'poster_path', 'origin_country', 'original_language', 'popularity']
                    add_keys = ['last_air_date']
                case _:
                    solicitacao = 'movie'
                    delete_keys = ['adult', 'backdrop_path', 'overview', 'poster_path', 'popularity', 'video', 'original_language']
                    add_keys = ['runtime']
            # convertendo lista de generos para um dicionário
            generos_all = {genre['id']:genre['name'] for genre in solicitacao_tmdb(f'genre/{solicitacao}/list')['genres']}
            # solicitando o retorno de paginas diferentes
            for num in range(1, 11):
                data = solicitacao_tmdb(search + f'?page={num}')
                conteudo = data['results']
                # adicionando ao retorno apenas se tiver algum dos generos escolhidos
                for item in conteudo:
                    for ids in item['genre_ids']:
                        if ids in genre_ids:
                            conteudo_final.append(item)
                            break
                # retirando chaves que não serão utilizadas
                [[item.pop(chave,None) for chave in delete_keys] for item in conteudo_final]
                for item in conteudo_final:
                    # se o valor do genero ainda não tiver sido convertido
                    if any(type(genre_id) == int for genre_id in item['genre_ids']):
                        mudancas = []
                        # adiciona o nome dos generos a lista temporaria
                        for genre_id in item['genre_ids']:
                            mudancas.append((generos_all[genre_id], genre_id))
                        # retira os id's dos generos e adiciona seus nomes
                        for mudanca in mudancas:
                            item['genre_ids'].remove(mudanca[1])
                            item['genre_ids'].append(mudanca[0])
                        # adiciona informações se necessário
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
            # organizando informações para enviar arquivo para o bucket
            s3 = boto3.client('s3')
            data_atual = datetime.now().strftime("%Y/%m/%d")
            bucket_name = 'projeto-tmdb'
            key = f'Raw/TMDB/JSON/{tipo.capitalize()}/{data_atual}/{tipo}.json'
            
            # converte dicionario para JSON
            json_data = json.dumps(data, ensure_ascii=False, indent=4)
            # envia arquivo para o bucket
            s3.put_object(Bucket=bucket_name, Key=key, Body=json_data.encode('utf-8'), ContentType='application/json')


        # otimização do processo
        for requisicao in [('tv/popular','series'), ('movie/popular', 'movies')]:
            data = tratar_dados(requisicao[0], requisicao[1])
            enviar_para_nuvem(data, requisicao[1])
        ```
    - Dockerfile

        ```dockerfile
        # imagem utilizada
        FROM public.ecr.aws/sam/build-python3.11

        # copia o bash script para o WORKDIR
        COPY create_layer . 

        # atualiza o gerenciador de pacotes
        RUN yum update -y

        # instala os pacotes que serão utilizados
        RUN yum install -y \
        python3-pip \
        zip

        # limpa o cache do gerenciador de pacotes
        RUN yum -y clean all
        ```
    - Bash script

        ```bash
        #!/bin/bash


        # verifica se arquivo está presente na pasta bin/ do usuário
        # se não estiver, adiciona
        if [ ! -f "/usr/local/bin/create_layer" ]; then
            cp create_layer /usr/local/bin/
            chmod +x /usr/local/bin/create_layer
        fi

        deletar=false

        # itera pelas flags repassadas
        while getopts "d" opt; do
            case $opt in
                d) deletar=true ;;
            esac
        done

        # se a flag -d for utilizada, a pasta da camada, se existir, é removida
        if [ "$deletar" = true ]; then
            if [ -d "/root/layer_dir" ]; then
                cd ~
                rm -rf /root/layer_dir
            fi
        else
            # cria as pastas necessárias e vai até o diretório criado
            mkdir -p ~/layer_dir/python
            cd ~/layer_dir/python

            # verifica se o caminho está de acordo com o esperado
            if [[ ! "$(pwd)" == "/root/layer_dir/python" ]]; then
                echo "Diretório errado! Abortando operação..."
            else
                # instala os pacotes repassados ao script no diretório atual
                echo "Instalando pacotes: $@"
                pip3 install "$@" -t .
                echo "Criando camada."
                # retorna uma camada e zipa o diretório que contém os pacotes instalados
                cd .. && zip -r minha_camada.zip .
                echo "Operação finalizada!"

                # vai até a pasta home/ do usuário e mostra a árvore de pastas para verificar se tudo ocorreu conforme planejado
                cd ~
                if [ ! -f "/usr/bin/tree" ]; then
                    yum install -q -y tree
                fi
                tree -L 3
            fi
        fi
        ```
    - Execução

        ```bash
        # montando imagem
        docker build -t amazonlinuxpython311 .
        ```
        ![build](/Sprint7/Evidencias/desafio/etapa-2/build.png)
        ```bash
        # subindo container
        docker run -it --rm amazonlinuxpython311 bash

        # tornando bash script executável
        chmod +x create_layer.bash # (versão antiga)

        # movendo o script e indo até a pasta root
        mv create_layer ~/ && cd ~
        # não é mais necessário fazer isso na versão mais recente do arquivo, apenas executar 'source create_layer <args>'.
        ```
        ![run](/Sprint7/Evidencias/desafio/etapa-2/preparando_execucao.png)
        ```bash
        # executando script
        ./create_layer.bash requests # (versão antiga)
        ```
        ![executando_bash_script](/Sprint7/Evidencias/desafio/etapa-2/executando_script.png)
        ![estrutura](/Sprint7/Evidencias/desafio/etapa-2/estrutura.png)
        ```bash
        # copiando zip do container para a pasta do projeto
        docker cp <id_container>:/root/layer_dir/minha_camada.zip ./
        ```
        ![cp zip](/Sprint7/Evidencias/desafio/etapa-2/copiando_zip.png)
    - Carregando camada para o bucket:

        ![carregando_camada_bucket](/Sprint7/Evidencias/desafio/etapa-2/carregando_camada_para_bucket.png)
    - Criando Lambda Function:
        
        ![criando_lambda](/Sprint7/Evidencias/desafio/etapa-2/criando_lambda_function.png)
    - Implementando python script:

        ![implementando](/Sprint7/Evidencias/desafio/etapa-2/codigo_implementado.png)
    - Criando Layer:

        ![criando_layer](/Sprint7/Evidencias/desafio/etapa-2/criando_layer.png)
    - Adicionando Layer à função Lambda:

        ![adicionando_layer_a_lambda](/Sprint7/Evidencias/desafio/etapa-2/adicionando_layer.png)
    - Adicionando permissão para a função Lambda:

        ![adicionando_perm](/Sprint7/Evidencias/desafio/etapa-2/permissao_ao_s3_concedida.png)
    - Adicionando API Key:
        
        ![add_api_key](/Sprint7/Evidencias/desafio/etapa-2/adicionando_variavel_de_ambiente.png)
    - Resultado da execução:

        ![resultado_movies](/Sprint7/Evidencias/desafio/etapa-2/execucao_sucesso_movies.png)
        ![resultado_series](/Sprint7/Evidencias/desafio/etapa-2/execucao_sucesso_series.png)
