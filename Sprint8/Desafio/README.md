# Desafio

## Sumário
- [Montando ambiente para desenvolvimento local](#et1)
- [Desenvolvimento - Manipulação de dados com Spark](#et2)
- [Glue](#et3)
- [Crawler](#et4)
- [Athena](#et5)

## <a name="et1">Montando ambiente para desenvolvimento local</a>
- [Dockerfile](/Sprint8/Desafio/arquivos/Dockerfile)
    
    ```Dockerfile
    # imagem que contém o ambiente com Spark
    FROM jupyter/all-spark-notebook

    # diretório para onde os arquivos serão persistidos
    # e onde iremos rodar os scripts
    WORKDIR /workspace
    ```
- [docker-compose.yaml](/Sprint8/Desafio/arquivos/docker-compose.yaml)
    
    ```yaml
    services:
        app:
            build:
                # local onde o Dockerfile se encontra
                context: .
                # nome do arquivo
                dockerfile: Dockerfile
            # nome do container
            container_name: spark-app
            # nome da imagem que o container irá rodar
            image: spark-app-image
            # diretório que será persistido para o WORKDIR
            volumes:
                - ./:/workspace:cached
            # evita que o container encerre sua execução
            command: sleep infinity
    ```
- Comandos:

    ```bash
    # adicionei os arquivos JSON e CSV a pasta que contém o Dockerfile e docker-compose.yaml
    # fui até o diretório e executei:
    docker compose up

    # abri uma nova sessão no terminal e acessei o container com:
    docker exec -it spark-app bash

    # criei um arquivo python para a modelagem e a cada alteração, testei o códico com:
    spark-submit *.py
    ```

## <a name="et2">Desenvolvimento - Manipulação de dados com Spark</a>
- [movies (py)](/Sprint8/Desafio/arquivos/movies.py)

    ```python
    # Junção do arquivo movies.json e movies.csv em um só DataFrame, otimização e conversão para Parquet.  

    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col, split, year, round, array_contains, when, monotonically_increasing_id, lit
    from datetime import datetime

    # utilizado para criar uma sessão localmente, retirado após enviar para o AWS Glue
    spark = SparkSession.builder.master("local[*]").appName("Create Trusted Movies").getOrCreate()

    # variáveis de ambiente guardadas nas configurações do job do Glue
    source_json_file = args['S3_JSON_MOVIES_PATH']
    source_csv_file = args['S3_CSV_MOVIES_PATH']
    target_path = args['TARGET_PATH']

    # gerando DataFrame a partir do json
    # multiline necessário por se tratar de uma lista de dicionários
    dados_json = spark.read.format("json").option("multiline", True).load(source_json_file)
    
    # gerando DataFrame a partir do csv
    # necessário especificar que possui header e que tem | como separador
    dados_csv = spark.read.format("csv").option("header", True).option("sep", "|").load(source_csv_file)

    # removendo colunas que não serão utilizadas
    dados_csv = dados_csv.drop("id", "personagem", "nomeArtista", "anoNascimento", "anoFalecimento", "profissao", "titulosMaisConhecidos", "generoArtista", "tituloOriginal", "numeroVotos")
    # renomeando colunas para gerar um padrão e futuramente unir DataFrame's
    dados_csv = dados_csv.withColumnsRenamed({"tituloPincipal": "titulo", "anoLancamento": "decada"})
    # excluindo linhas duplicadas levando apenas `titulo` em consideração
    dados_csv = dados_csv.dropDuplicates(["titulo"])
    # alterando string com itens separados por `,` para um array
    dados_csv = dados_csv.withColumn("genero", split("genero", ","))
    # filtrando apenas linhas que possuem os generos desejados
    dados_csv = dados_csv.filter(
            array_contains("genero", "Comedy")
            | array_contains("genero", "Animation")
    )
    # dividindo o ano por 10 e após multiplicando por 10 para obter a década
    dados_csv = dados_csv.withColumn("decada", (col("decada")/10).cast("int") * 10)
    # arredondando `notaMedia` para ter apenas uma casa decimal após a vírgula
    dados_csv = dados_csv.withColumn("notaMedia", round("notaMedia", 1))

    # removendo colunas que não serão utilizadas
    dados_json = dados_json.drop("id", "original_title", "vote_count")
    # renomeando colunas para gerar um padrão e futuramente unir DataFrame's
    dados_json = dados_json.withColumnsRenamed({"genre_ids": "genero", "release_date": "decada", "runtime": "tempoMinutos", "title": "titulo", "vote_average": "notaMedia"})
    # dividindo o ano por 10 e após multiplicando por 10 para obter a década
    # year() necessário pois campo também possui mes e dia
    dados_json = dados_json.withColumn("decada", (year("decada")/10).cast("int") * 10)
    # arredondando `notaMedia` para ter apenas uma casa decimal após a vírgula
    dados_json = dados_json.withColumn("notaMedia", round("notaMedia", 1))

    # juntando DataFrame's
    dados_movies = dados_csv.unionByName(dados_json)
    # excluindo linhas duplicadas levando apenas `titulo` em consideração
    dados_movies = dados_movies.dropDuplicates(["titulo"])
    # ordenando em ordem crescente por `titulo`
    dados_movies = dados_movies.orderBy("titulo")

    # substituindo campos que possuem \N por None (NULL no DataFrame)
    dados_movies = dados_movies.withColumn(
            "tempoMinutos",
            when(col("tempoMinutos") == r"\N", None).otherwise(col("tempoMinutos"))
    )
    # adicionando um id a todas as linhas do DataFrame
    dados_movies = dados_movies.withColumn("id", monotonically_increasing_id())

    # pegando a data atual
    now = datetime.now()
    # criando colunas ano, mes e dia para poder particionar por elas
    dados_movies = dados_movies \
            .withColumn("ano", lit(now.year)) \
            .withColumn("mes", lit(now.month)) \
            .withColumn("dia", lit(now.day))
    # salvando arquivo no formato pedido
    dados_movies.write.mode("overwrite").partitionBy("ano", "mes", "dia").format("parquet").save(target_path)
    ```
- [series (py)](/Sprint8/Desafio/arquivos/series.py)

    ```python
    # Junção do arquivo series.json e series.csv em um só DataFrame, otimização e conversão para Parquet. 

    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col, split, year, round, array_contains, when, monotonically_increasing_id, lit
    from datetime import datetime

    # utilizado para criar uma sessão localmente, retirado após enviar para o AWS Glue
    spark = SparkSession.builder.master("local[*]").appName("Create Trusted Series").getOrCreate()

    # variáveis de ambiente guardadas nas configurações do job do Glue
    source_json_file = args['S3_JSON_SERIES_PATH']
    source_csv_file = args['S3_CSV_SERIES_PATH']
    target_path = args['TARGET_PATH']

    # gerando DataFrame a partir do json
    # multiline necessário por se tratar de uma lista de dicionários
    dados_json = spark.read.format("json").option("multiline", True).load(source_json_file)

    # gerando DataFrame a partir do csv
    # necessário especificar que possui header e que tem | como separador
    dados_csv = spark.read.format("csv").option("header", True).option("sep", "|").load(source_csv_file)

    # removendo colunas que não serão utilizadas
    dados_json = dados_json.drop("id", "original_name", "vote_count")
    # renomeando colunas para gerar um padrão e futuramente unir DataFrame's
    dados_json = dados_json.withColumnsRenamed({"genre_ids": "genero", "name": "titulo", "vote_average": "notaMedia", "first_air_date": "anoLancamento", "last_air_date": "anoTermino"})
    # dividindo o ano por 10 e após multiplicando por 10 para obter a década
    # year() necessário pois campo também possui mes e dia
    dados_json = dados_json.withColumn("decada", (year("anoLancamento")/10).cast("int") * 10)
    # alterando campos com data composta para apenas conter o ano
    dados_json = dados_json.withColumn("anoLancamento", year("anoLancamento"))
    # substituindo campos que possuem \N por None (NULL no DataFrame)
    # caso não possua \N, apenas o ano será salvo no campo
    dados_json = dados_json.withColumn(
            "anoTermino",
            when(col("anoTermino") == r"\N", None)
            .otherwise(year(col("anoTermino")))
    )
    # arredondando `notaMedia` para ter apenas uma casa decimal após a vírgula
    dados_json = dados_json.withColumn("notaMedia", round("notaMedia", 1))

    # removendo colunas que não serão utilizadas
    dados_csv = dados_csv.drop("id", "tituloOriginal", "tempoMinutos", "numeroVotos", "generoArtista", "personagem", "nomeArtista", "anoNascimento", "anoFalecimento", "profissao", "titulosMaisConhecidos")
    # renomeando colunas para gerar um padrão e futuramente unir DataFrame's
    dados_csv = dados_csv.withColumnsRenamed({"tituloPincipal": "titulo"})
    # excluindo linhas duplicadas levando apenas `titulo` em consideração
    dados_csv = dados_csv.dropDuplicates(["titulo"])
    # alterando string com itens separados por `,` para um array
    dados_csv = dados_csv.withColumn("genero", split("genero", ","))
    # filtrando apenas linhas que possuem os generos desejados
    dados_csv = dados_csv.filter(
            array_contains("genero", "Comedy")
            | array_contains("genero", "Animation")
    )
    # dividindo o ano por 10 e após multiplicando por 10 para obter a década
    dados_csv = dados_csv.withColumn("decada", (col("anoLancamento")/10).cast("int") * 10)
    # substituindo campos que possuem \N por None (NULL no DataFrame)
    dados_csv = dados_csv.withColumn(
            "anoTermino",
            when(col("anoTermino") == r"\N", None)
            .otherwise(col("anoTermino"))
    )
    # arredondando `notaMedia` para ter apenas uma casa decimal após a vírgula
    dados_csv = dados_csv.withColumn("notaMedia", round("notaMedia", 1))

    # juntando DataFrame's
    dados_series = dados_csv.unionByName(dados_json)
    # excluindo linhas duplicadas levando apenas `titulo` em consideração
    dados_series = dados_series.dropDuplicates(["titulo"])
    # ordenando em ordem crescente por `titulo`
    dados_series = dados_series.orderBy("titulo")

    # criando coluna `ativo`
    # se `anoTermino` for NULL, `ativo` também será
    # se não, é calculada a diferença entre anoLancamento e anoTermino somado a um
    dados_series = dados_series.withColumn(
            "ativo", 
            when(col("anoTermino") == "NULL", None)
            .otherwise((col("anoTermino")-col("anoLancamento")+1).cast("int"))
    )
    # removendo colunas que não serão utilizadas
    dados_series = dados_series.drop("anoLancamento", "anoTermino")
    # adicionando um id a todas as linhas do DataFrame
    dados_series = dados_series.withColumn("id", monotonically_increasing_id())

    # pegando a data atual
    now = datetime.now()
    # criando colunas ano, mes e dia para poder particionar por elas
    dados_series = dados_series \
            .withColumn("ano", lit(now.year)) \
            .withColumn("mes", lit(now.month)) \
            .withColumn("dia", lit(now.day))
    # salvando arquivo no formato pedido
    dados_series.write.mode("overwrite").partitionBy("ano", "mes", "dia").format("parquet").save(target_path)
    ```

## <a name="et3">Glue</a>
- Criando IAM Role

    ![criando_iam_role](/Sprint8/Evidencias/desafio/iam_role/criando_iam_role.png)
- Adicionando permissões

    ![perm_iam_role](/Sprint8/Evidencias/desafio/iam_role/adicionando_permissoes.png)
- Nomeando IAM Role

    ![nomeando_iam_role](/Sprint8/Evidencias/desafio/iam_role/nomeando_iam_role.png)
- Criando Job (etapa realizada para filmes e series)

    ![criando_job](/Sprint8/Evidencias/desafio/glue/criando_job_movies.png)
- Adicionando Parâmetros (etapa realizada para filmes e series)

    ![parametros_glue](/Sprint8/Evidencias/desafio/glue/criando_parametros_movies.png)
- Colando código revisado localmente em Script (etapa realizada para filmes e series)

    ![codigo_glue](/Sprint8/Evidencias/desafio/glue/adicionando_codigo_movies.png)
- Rodando Job (etapa realizada para filmes e series)

    ![rodando_job](/Sprint8/Evidencias/desafio/glue/rodando_job_movies.png)
- Resultado do Job

    ![resultado_movies](/Sprint8/Evidencias/desafio/glue/monitoramento_job_movies.png)
    ![resultado_series](/Sprint8/Evidencias/desafio/glue/monitorando_job_series.png)
- Parquet's gerados

    ![s3_movies](/Sprint8/Evidencias/desafio/s3/parquet_gerado_movies.png)
    ![s3_series](/Sprint8/Evidencias/desafio/s3/parquet_gerado_series.png)
## <a name="et4">Crawler</a>
- Setando Propriedades

    ![setando_prop](/Sprint8/Evidencias/desafio/crawler/setando_propriedades_crawler.png)
- Apontando caminho para Parquet's

    ![source_files](/Sprint8/Evidencias/desafio/crawler/adicionando_parquet.png)
- Setando IAM Role

    ![config_crawler](/Sprint8/Evidencias/desafio/crawler/config_seguranca_crawler.png)
- Criando Database

    ![criando_db](/Sprint8/Evidencias/desafio/crawler/criando_database_no_glue_data_catalog.png)
- Criando Crawler

    ![criando_crawler](/Sprint8/Evidencias/desafio/crawler/criando_crawler.png)
- Rodando Crawler

    ![rodando_crawler](/Sprint8/Evidencias/desafio/crawler/rodando_crawler.png)
- Tabelas geradas

    ![tabelas_geradas](/Sprint8/Evidencias/desafio/crawler/tabelas_geradas.png)
    ![tabela_movies](/Sprint8/Evidencias/desafio/crawler/movies.png)
    ![tabela_series](/Sprint8/Evidencias/desafio/crawler/series.png)
## <a name="et5">Athena</a>
- Configurando o AWS Athena

    ![config_athena](/Sprint8/Evidencias/desafio/athena/athena_config.png)
- Testando Query (Movies)

    ![athena_movies](/Sprint8/Evidencias/desafio/athena/athena_movies.png)
- Testando Query (Series)

    ![athena_series](/Sprint8/Evidencias/desafio/athena/athena_series.png)