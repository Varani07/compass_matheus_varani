# Resumo
## Sumário

- [Desafio](#desafio)
- [Cursos](#cursos)
    - [Formação Spark com PySpark: O Curso Completo](#curso-pyspark)
    - [Noções Básicas de Analytics na AWS - Parte 1](#analytics-parte-1)
- [Exercícios](#exercicios)
    - [Apache Spark - Contadorde palavras](#ex1)
    - [Exercícios TMDB](#ex2)

## <a name="desafio">Desafio</a>
Pasta contendo arquivos e README.md referente ao desafio proposto:
- [Pasta do desafio](/Sprint7/Desafio/)
- [README.md do desafio](/Sprint7/Desafio/README.md)

## <a name="cursos">Cursos</a>
### <a name="curso-pyspark">***Formação Spark com PySpark: O Curso Completo***</a>
- Instalar o Oracle Virtual Box e configurá-lo.
- Preparar o ambiente para a instação do Spark.
- Principais características do Spark:
    - Capacidade de processar dados em memória;
    - Opera em Cluster;
    - Capaz de particionar os dados;
    - Paralelismo;
    - Redundância.

### <a name="analytics-parte-1">***Noções Básicas de Analytics na AWS - Parte 1***</a>
- Benefícios do data analytics:
    - Encontrar padrões;
    - Descobrir oportunidades;
    - Prever eventos e ações;
    - Tomar decisões bem informadas.

- Tipos de analytics:
    - Descritiva (O que aconteceu?);
    - Diagnóstica (Por que algo aconteceu?);
    - Preditiva (O que pode acontecer no futuro?);
    - Prescritiva (Recomenda ações para alcançar o resultado previsto).

- 5 Vs:
    - Volume, Quantidade de dados;
    - Variedade, Quantidade de diferentes fontes;
    - Velocidade, Velocidade de processamento dos dados;
    - Veracidade, Precisão dos dados;
    - Valor, O quanto de informações significativas se consegue a partir dos dados.

- Serviços da AWS:
    - Para volume:
        - Amazon S3: Armazene qualquer quantidade de objetos com escalabilidade, disponibilidade e segurança. 
        - AWS Lake Formation: onstrua, gerencie e proteja data lakes de forma mais rápida e fácil.
        - Amazon Redshift: Utilize data warehousing na núvem com o melhor custo-benefício.
    - Para variedade:
        - Amazon RDS: Banco de dados relacional baseado na nuvem para fácil configuração, operação e escalabilidade.
        - Amazon Redshift: Melhor relação preço/desempenho para armazenamento de dados na nuvem.
        - Amazon OpenSearch Service: Pesquisa, monitoramento e análise em tempo real de dados empresariais e operacionais.
        - Amazon DynamoDB: Banco de dados NoSQL rápido, flexível e totalmente gerenciado para alto desempenho em qualquer escala.

    - Para velocidade:
        - Amazon EMR: Solução de big data para processamento de dados em escala de petabytes, análise interativa e ML.
        - Amazon MSK: Serviço Apache Kafka totalmente gerenciado e altamente disponível.
        - Amazon Kinesis: Serviço econômico para processar e analisar dados de streaming em qualquer escala como um serviço totalmente gerenciado.
        - AWS Lambda: Serviço computacional com tecnologia sem servidor e orientado por eventos, que permite que você execute o código sem provisionar ou gerenciar servidores.

    - Para variedade:
        - Amazon EMR: Simplifique a coleta e o processamento de dados para workloads de big data.
        - Amazon Glue: Prepare e integre todos os seus dados em qualquer escala.
        - AWS Glue DataBrew: Limpe e normalize os dados com mais rapidez e eficiência.
        - Amazon DataZone: Compartilhe dados em toda a organização com governança integrada.
        
    - Para valor:
        - Amazon QuickSight: Business intelligence unificado em escala de nuvem.
        - Amazon SageMaker: Crie, treine e implante modelos de ML para qualquer caso de uso com infraestrutura. ferramentas e fluxos de trabalho totalmente gerenciados.
        - Amazon Bedrock: Crie e escale aplicações de IA generativa com modelos de base.
        - Amazon Athena: Analise dados em escala de petabytes onde eles estiverem.

### <a name="athena-intro">***Introduction to Amazon Athena***</a>
- Apresentação geral sobre o serviço Amazon Athena;
- Etapas básicas para a implementação do serviço;
- Exemplo prático.

### <a name="serverless-analytics">***Serverless Analytics***</a>
- Uso para o serviço AWS IoT Analytics, Amazon Cognito, AWS Lambda e Amazon SageMaker;
- Modelagem de dados.

## <a name="exercicios">***Exercícios***</a>
### <a name="ex1">***Apache Spark - Contadorde palavras***</a>
- Objetivo: Desenvolver um job de processamento com o framework Spark por meio de um container Docker.

- Arquivos:
    - [Dockerfile utilizado para criar a imagem utilizada nessa atividade.](/Sprint7/Exercicios/ex1/Dockerfile)
    - [Comandos utilizados para cumprir com a atividade proposta.](/Sprint7/Exercicios/ex1/comandos.txt)

- Passo a passo:
    - Dockerfile
        ```Dockerfile
        # definindo imagem que será utilizada
        FROM jupyter/all-spark-notebook

        # diretório onde o projeto irá rodar
        WORKDIR /work

        # copiando arquivo que será utilizado para dentro do WORKDIR
        COPY README.md .

        # expondo porta para que seja possível acessar o jupyter notebook fora do container
        EXPOSE 8888
        ```
    - Comandos Docker
        ```bash
        # 
        ```

        ```bash
        # baixando imagem que será utilizada na build
        docker pull jupyter/all-spark-notebook
        ```
        ![pull](/Sprint7/Evidencias/exercicios/ex1/pull.png)
        ```bash
        # montando imagem 
        docker build -f Sprint7/Exercicios/ex1/Dockerfile -t contar_palavras .

        # precisa ser executado a partir da pasta raiz do projeto
        # -f especifica o local do Dockerfile
        # -t dá um nome a imagem
        # precisamos fazer dessa forma para copiar o arquivo README.md para dentro do container
        ```
        ![build](/Sprint7/Evidencias/exercicios/ex1/build.png)
        ```bash
        # subindo o container
        docker run -p 8888:8888 -it --name conta_palavras --rm contar_palavras

        # -p especifica a porta a ser utilizada
        # -it roda o container em modo interativo
        # --name nomeia o container
        # --rm remove o container assim que para de rodar
        ```
        ![run](/Sprint7/Evidencias/exercicios/ex1/run.png)
        ![ps](/Sprint7/Evidencias/exercicios/ex1/ps.png)
        ```bash
        # acessando container
        docker exec -it conta_palavras bash
        ```
        ![exec](/Sprint7/Evidencias/exercicios/ex1/exec.png)
    - Interagindo com o Spark
        ```bash
        # acessando o shell spark
        pyspark
        ```
        ![pyspark](/Sprint7/Evidencias/exercicios/ex1/pyspark.png)
        ```bash
        # fazendo os imports necessários
        from pyspark.sql.functions import explode, split
        ```
        ```bash
        # gerando DataFrame a partir do READ.me
        df = spark.read.text("README.md")
        ```
        ```bash
        # transformações necessárias para contar palavras
        word_counts = df.select(explode(split("value", " ")).alias("word")).groupBy("word").count()

        # split(col, valor) divide os itens da coluna pelo valor definido, retornando uma lista de strings
        # explode() transforma cada string presente na lista em um item no DataFrame
        # alias() define o nome da coluna
        # groupBy(col) agrupa os itens da coluna definida
        # count() conta quantas vezes o item está presente no DataFrame  
        ```
        ```bash
        # salvando resultado
        word_counts.write.format("json").save("/work/word_count")
        
        # format() formato desejado
        # save() caminho onde será salvo
        ```
        ![spark_shell](/Sprint7/Evidencias/exercicios/ex1/spark_shell.png)
        ```bash
        # saindo do spark shell e verificando resultado
        exit()
        cat -n word_count/*json
        ```
        ![verificando](/Sprint7/Evidencias/exercicios/ex1/verificando.png)

### <a name="ex2">***Exercícios TMDB***</a>
- Objetivo: Criar um processo de extração de dados da API do TMDb utilizando os serviços da AWS (Apesar de estar no objetivo, não é há nenhuma instrução sobre algum serviço da AWS no documento).

- Arquivos:
    - [Código.](/Sprint7/Exercicios/ex2/tmdb_api.py)

- Passo a passo:
    - Já tinha uma conta no site do TMDb, então só precisei logar.
    - Resgatei minha chave da API e coloquei em meu arquivo `.env`.
    - Python file:
        - Realizando imports necessários:

            ```python
            import requests, os, json
            from dotenv import load_dotenv
            import pandas as pd
            ```
        - Carregando variáveis para o ambiente e guardando o valor da chave API:

            ```python
            load_dotenv()
            api_key = os.getenv("TMDB_API_KEY")
            ```
        - Definindo função para buscar os dados do TMDb:

            ```python
            def info_filmes() ->str:
            ```
        - Montando argumentos que serão passados para fazer a requisição:

            ```python
            url = f"https://api.themoviedb.org/3/genre/movie/list?language=en"
            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
            ```
        - Efetuando requisição e retornando seu resultado.

            ```python
            response = requests.get(url, headers=headers)
            
            # text é utilizado para retornar o conteúdo da requisição
            return response.text
            ```

        ```python
        # json.loads transforma a string em um dicionário
        data = json.loads(info_filmes())

        # especificando o conteúdo do retorno que desejamos
        data = data['genres']

        # transformando a lista de dicionários em um DataFrame e printando o resultado
        df = pd.DataFrame(data)
        print(df)
        ```
        ![print](/Sprint7/Evidencias/exercicios/ex2/print.png)
