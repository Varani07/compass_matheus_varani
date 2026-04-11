# Desafio

## Sumário
- [Montando ambiente para desenvolvimento local](#et1)
- [Desenvolvimento - Manipulação de dados com Spark](#et2)
- [Glue](#et3)
- [Crawler](#et4)
- [Athena](#et5)
- [Análises Geradas com o QuickSight](#et6)

## <a name="et1">Montando ambiente para desenvolvimento local</a>
- [Dockerfile](/Sprint8/Desafio/arquivos/Dockerfile)
    
    ```Dockerfile
    # imagem que contém o ambiente com Spark
    FROM jupyter/all-spark-notebook

    # diretório para onde os arquivos serão persistidos
    # e onde iremos rodar o script
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
    # adicionei os arquivos PARQUET a pasta que contém o Dockerfile e docker-compose.yaml
    # fui até o diretório e executei:
    docker compose up -d
    # -d roda o container em background
    ```
    ![up](../Evidencias/desafio/local-dev/up.png)
    ```bash
    # abri uma nova sessão no terminal e acessei o container com:
    docker exec -it spark-app bash
    ```
    ![exec](../Evidencias/desafio/local-dev/exec.png)
    ```bash
    # criei um arquivo python para a modelagem e a cada alteração, testei o códico com:
    spark-submit *.py
    ```
## <a name="et2">Desenvolvimento - Manipulação de dados com Spark</a>
- tabelas
    ![alt text](../Evidencias/desafio/diagrama/tabelas.png)
- views
    ![alt text](../Evidencias/desafio/diagrama/views.png)
- [glue script (py)](/Sprint9/Desafio/arquivos/glue.py)

    ```python
    # realizando imports necessários
    from pyspark.sql import SparkSession
    from pyspark.sql.window import Window
    from pyspark.sql.functions import col, when, lit, explode, row_number

    # utilizado para criar uma sessão localmente, retirado após enviar para o AWS Glue
    spark = SparkSession.builder.master("local[*]").appName("teste").getOrCreate()

    # variáveis de ambiente guardadas nas configurações do job do Glue
    source_movies = args['MOVIES_PATH']
    source_series = args['SERIES_PATH']
    target_path = args['TARGET_PATH']
    target_view_path = args['TARGET_VIEW_PATH']

    # gerando DataFrame's
    df_series = spark.read.parquet(source_series)
    df_movies = spark.read.parquet(source_movies)

    # criando coluna para separar os filmes das séries após junção
    # dos DataFrame's
    df_movies = df_movies.withColumn("tipo", lit("movie"))
    df_series = df_series.withColumn("tipo", lit("serie"))

    # criando tabelas únicas de cada tipo e associando NULL a elas
    df_movies = df_movies.withColumn("ativo", lit(None))
    df_series = df_series.withColumn("tempoMinutos", lit(None))

    # unindo DataFrame's
    df = df_series.unionByName(df_movies)
    # retirando colunas que não serão utilizadas
    df = df.drop("dia", "mes", "ano")
    # renomeando colunas para gerar um padrão
    df = df.withColumnsRenamed({"notaMedia": "nota_media", "tempoMinutos": "tempo_minutos", "id": "id_conteudo"})
    # retirando todas as séries que pessuem NULL no campo `decada`
    df = df.where((col("decada").isNotNull()) | (col("tipo") != lit("serie")))
    # alterando todas as linhas que possuem NULL como valor da coluna
    # `decada` para -1
    df = df.withColumn("decada", when(col("decada").isNull(), -1).otherwise(col("decada")))
    # criando Window e definindo ordem para criar id's
    window_spec_conteudo = Window.orderBy("tipo", "titulo")
    # gerando id's
    df = df.withColumn("id_conteudo", row_number().over(window_spec_conteudo))

    # selecionando todas as decadas com distinct()
    dim_decada = df.select("decada").distinct()
    # criando Window e definindo ordem para criar id's
    window_spec_decada = Window.orderBy("decada")
    # gerando id's
    dim_decada = dim_decada.withColumn("id_decada", row_number().over(window_spec_decada))

    # explodindo arrays presentes na coluna `genero`
    df_exploded = df.withColumn("genero", explode(col("genero")))
    # selecionando todos os generos com distinct()
    dim_genero = df_exploded.select("genero").distinct()
    # criando Window e definindo ordem para criar id's
    window_spec_genero = Window.orderBy("genero")
    # gerando id's
    dim_genero = dim_genero.withColumn("id_genero", row_number().over(window_spec_genero))
    # criando bridge com join
    # necessário pois cada serie/filme pode possuir um ou mais generos
    bridge_conteudo_genero = df_exploded.select("genero", "id_conteudo").join(dim_genero, on="genero", how="inner").select("id_conteudo", "id_genero")

    # criando fato com join para conseguir fazer uso do id das decadas
    fato_conteudo = df.join(dim_decada, on="decada", how="inner").select("id_conteudo", "id_decada", "nota_media")
    # criando dim com as colunas selecionadas
    dim_conteudo = df.select("id_conteudo", "titulo", "tipo", "tempo_minutos", "ativo")

    # organizando informações em conjunto com o tipo de cada coluna
    fato_conteudo = fato_conteudo.select(
        col("id_conteudo").cast("long"),
        col("id_decada").cast("int"),
        col("nota_media").cast("double")
    )
    dim_conteudo = dim_conteudo.select(
        col("id_conteudo").cast("long"),
        col("titulo").cast("string"),
        col("tipo").cast("string"),
        col("tempo_minutos").cast("int"), # null
        col("ativo").cast("int") # null
    )
    dim_genero = dim_genero.select(
        col("id_genero").cast("int"),
        col("genero").cast("string")
    )
    dim_decada = dim_decada.select(
        col("id_decada").cast("int"),
        col("decada").cast("int")
    )
    bridge_conteudo_genero = bridge_conteudo_genero.select(
        col("id_conteudo").cast("long"),
        col("id_genero").cast("int")
    )

    # criando views com os seguintes DataFrame's para efetuar as queries
    fato_conteudo.createOrReplaceTempView("fato")
    dim_conteudo.createOrReplaceTempView("conteudo")
    dim_decada.createOrReplaceTempView("decada")
    dim_genero.createOrReplaceTempView("genero")
    bridge_conteudo_genero.createOrReplaceTempView("conteudo_genero")

    # selecionamos o tempo em minutos e a media da nota 
    # de todos os filmes de comedia em que o tempo em minutos não é NULL
    # ordenando de forma crescente pelo tempo em minutos
    relacao_duracao_nota_filmes_comedia = spark.sql("""
    SELECT c.tempo_minutos, f.nota_media
    FROM fato f
    JOIN conteudo c ON f.id_conteudo = c.id_conteudo
    JOIN conteudo_genero cg ON c.id_conteudo = cg.id_conteudo
    JOIN genero g ON cg.id_genero = g.id_genero
    WHERE c.tipo = 'movie' AND g.genero = 'Comedy' AND c.tempo_minutos IS NOT NULL 
    ORDER BY c.tempo_minutos;                                                
    """)

    # selecionamos a decada e a média da nota
    # de todos os filmes de comédia e/ou animação
    # em que a decada não for -1
    # ordenando de forma crescente pela decada
    relacao_decada_nota_filmes_comedia_animacao = spark.sql("""
    SELECT d.decada, f.nota_media
    FROM fato f
    JOIN conteudo c ON f.id_conteudo = c.id_conteudo
    JOIN conteudo_genero cg ON c.id_conteudo = cg.id_conteudo
    JOIN genero g ON cg.id_genero = g.id_genero
    JOIN decada d ON f.id_decada = d.id_decada
    WHERE (g.genero = 'Animation' OR g.genero = 'Comedy') AND c.tipo = 'movie' AND d.decada != -1
    ORDER BY d.decada;                                                  
    """)

    # selecionamos o tempo em que a série permaneceu ativa
    # e a média da nota de todas as séries de comédia e/ou animação
    # em que `ativo` não é NULL
    # ordenando de forma crescente pelo tempo em anos
    # que a série permaneceu ativa
    relacao_tempo_ativo_nota_series_comedia_animacao = spark.sql("""
    SELECT c.ativo, f.nota_media
    FROM fato f
    JOIN conteudo c ON f.id_conteudo = c.id_conteudo
    JOIN conteudo_genero cg ON c.id_conteudo = cg.id_conteudo
    JOIN genero g ON cg.id_genero = g.id_genero
    WHERE (g.genero = 'Animation' OR g.genero = 'Comedy') AND c.ativo IS NOT NULL AND c.tipo = 'serie'
    ORDER BY c.ativo;                                                 
    """)

    # selecionamos a decada e a média das notas de cada decada
    # de todos filmes e séries de animação em que a decada não é -1
    # agrupando e ordenando de forma crescente pela decada
    media_animacao_por_decada = spark.sql("""
    SELECT d.decada, ROUND(AVG(f.nota_media),1) AS media_nota
    FROM fato f
    JOIN conteudo c ON f.id_conteudo = c.id_conteudo
    JOIN conteudo_genero cg ON c.id_conteudo = cg.id_conteudo
    JOIN genero g ON cg.id_genero = g.id_genero
    JOIN decada d ON f.id_decada = d.id_decada
    WHERE g.genero = 'Animation' AND d.decada != -1
    GROUP BY d.decada
    ORDER BY d.decada;                                   
    """)

    # salvando tabelas
    fato_conteudo.write.mode("overwrite").partitionBy("id_decada").format("parquet").save(f"{target_path}fato_conteudo/")
    dim_conteudo.write.mode("overwrite").partitionBy("tipo").format("parquet").save(f"{target_path}dim_conteudo/")
    dim_decada.write.mode("overwrite").format("parquet").save(f"{target_path}dim_decada/")
    dim_genero.write.mode("overwrite").format("parquet").save(f"{target_path}dim_genero/")
    bridge_conteudo_genero.write.mode("overwrite").partitionBy("id_genero").format("parquet").save(f"{target_path}bridge_conteudo_genero/")

    # salvando views
    relacao_duracao_nota_filmes_comedia.write.mode("overwrite").format("parquet").save(f"{target_view_path}relacao_duracao_nota_filmes_comedia/")
    relacao_decada_nota_filmes_comedia_animacao.write.mode("overwrite").partitionBy("decada").format("parquet").save(f"{target_view_path}relacao_decada_nota_filmes_comedia_animacao/")
    relacao_tempo_ativo_nota_series_comedia_animacao.write.mode("overwrite").partitionBy("ativo").format("parquet").save(f"{target_view_path}relacao_tempo_ativo_nota_series_comedia_animacao/")
    media_animacao_por_decada.write.mode("overwrite").format("parquet").save(f"{target_view_path}media_animacao_por_decada/")
    ```
## <a name="et3">Glue</a>
- Criando job

    ![criando_job](../Evidencias/desafio/glue/criando_job.png)
- Definindo parâmetros do job

    ![definindo_parametros](../Evidencias/desafio/glue/definindo_parametros.png)
- Adicionando código que foi desenvolvido localmente ao Script do AWS Glue

    ![adicionando_codigo](../Evidencias/desafio/glue/adicionando_codigo.png)
- Rodando job

    ![rodando_job](../Evidencias/desafio/glue/rodando_job.png)
    ![sucesso_job](../Evidencias/desafio/glue/sucesso_job.png)
- Parquet's gerados

    ![s3_fato_conteudo](../Evidencias/desafio/s3/fato_conteudo.png)
    ![s3_dim_conteudo](../Evidencias/desafio/s3/dim_conteudo.png)
    ![s3_dim_decada](../Evidencias/desafio/s3/dim_decada.png)
    ![s3_dim_genero](../Evidencias/desafio/s3/dim_genero.png)
    ![s3_bridge_conteudo_genero](../Evidencias/desafio/s3/bridge_conteudo_genero.png)
## <a name="et4">Crawler</a>
- O mesmo processo a seguir foi realizado para as views
- Setando propriedades

    ![setando_prop](../Evidencias/desafio/crawler/setando_prop.png)
- Apontando caminho para Parquet's

    ![data_source](../Evidencias/desafio/crawler/data_source.png)
- Setando IAM Role

    ![setando_iam_role](../Evidencias/desafio/crawler/setando_iam_role.png)
- Criando Database

    ![criando_db](../Evidencias/desafio/crawler/criando_db.png)
- Setando Database

    ![setando_db](../Evidencias/desafio/crawler/setando_db.png)
- Criando Crawler

    ![criando_crawler](../Evidencias/desafio/crawler/criando_crawler.png)
- Rodando Crawler

    ![rodando_crawler](../Evidencias/desafio/crawler/rodando_crawler.png)
    ![sucesso_crawler](../Evidencias/desafio/crawler/sucesso_crawler.png)
- Tabelas geradas

    ![alt text](../Evidencias/desafio/crawler/movies_series.png)
    ![alt text](../Evidencias/desafio/crawler/views_movies_series.png)
    ![alt text](../Evidencias/desafio/crawler/fato_conteudo.png)
    ![alt text](../Evidencias/desafio/crawler/dim_conteudo.png)
    ![alt text](../Evidencias/desafio/crawler/dim_decada.png)
    ![alt text](../Evidencias/desafio/crawler/dim_genero.png)
    ![alt text](../Evidencias/desafio/crawler/bridge_conteudo_genero.png)
    ![alt text](../Evidencias/desafio/crawler/relacao_duracao_nota_filmes_comedia.png)
    ![alt text](../Evidencias/desafio/crawler/relacao_decada_nota_filmes_comedia_animacao.png)
    ![alt text](../Evidencias/desafio/crawler/relacao_tempo_ativo_nota_series_comedia_animacao.png)
    ![alt text](../Evidencias/desafio/crawler/media_animacao_por_decada.png)
## <a name="et5">Athena</a>
- Configurando o AWS Athena

    ![alt text](../Evidencias/desafio/athena/config_athena.png)
- Testando Query

    ![alt text](../Evidencias/desafio/athena/query_result.png)
    - Query:
    ```sql
    SELECT
        c.titulo,
        c.tipo,
        g.genero,
        d.decada,
        f.nota_media
    FROM
        fato_conteudo f
    JOIN
        dim_conteudo c ON f.id_conteudo = c.id_conteudo
    JOIN
        dim_decada d ON CAST(f.id_decada AS INTEGER) = d.id_decada
    JOIN
        bridge_conteudo_genero cg ON f.id_conteudo = cg.id_conteudo
    JOIN
        dim_genero g ON CAST(cg.id_genero AS INTEGER) = g.id_genero
    WHERE 
        (g.genero = 'Comedy' OR g.genero = 'Animation')
        AND d.decada != -1
    LIMIT 10;
    ```
## <a name="et6">Análises Geradas com o QuickSight</a>
- [Média da nota por Duração | Filmes de Comédia](/Sprint9/Desafio/analises/analise_1.pdf)
- [Distribuição de Notas de filmes por Era: Comédia e Animação](/Sprint9/Desafio/analises/analise_2.pdf)
- [Relação entre anos em Exibição e Avaliação Média | Séries de Comédia e Animação](/Sprint9/Desafio/analises/analise_3.pdf)
- [Média da nota por década | Comédia x Animação (1920-2020)](/Sprint9/Desafio/analises/analise_4.pdf)