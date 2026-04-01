from pyspark.sql import SparkSession
from pyspark.sql.functions import col, split, year, round, array_contains, when, monotonically_increasing_id, lit
from datetime import datetime


spark = SparkSession.builder.master("local[*]").appName("Create Trusted Movies").getOrCreate()

source_json_file = args['S3_JSON_MOVIES_PATH']
source_csv_file = args['S3_CSV_MOVIES_PATH']
target_path = args['TARGET_PATH']

dados_json = spark.read.format("json").option("multiline", True).load(source_json_file)
dados_csv = spark.read.format("csv").option("header", True).option("sep", "|").load(source_csv_file)

dados_csv = dados_csv.drop("id", "personagem", "nomeArtista", "anoNascimento", "anoFalecimento", "profissao", "titulosMaisConhecidos", "generoArtista", "tituloOriginal", "numeroVotos")
dados_csv = dados_csv.withColumnsRenamed({"tituloPincipal": "titulo", "anoLancamento": "decada"})
dados_csv = dados_csv.dropDuplicates(["titulo"])
dados_csv = dados_csv.withColumn("genero", split("genero", ","))
dados_csv = dados_csv.filter(
        array_contains("genero", "Comedy")
        | array_contains("genero", "Animation")
)
dados_csv = dados_csv.withColumn("decada", (col("decada")/10).cast("int") * 10)
dados_csv = dados_csv.withColumn("notaMedia", round("notaMedia", 1))

dados_json = dados_json.drop("id", "original_title", "vote_count")
dados_json = dados_json.withColumnsRenamed({"genre_ids": "genero", "release_date": "decada", "runtime": "tempoMinutos", "title": "titulo", "vote_average": "notaMedia"})
dados_json = dados_json.withColumn("decada", (year("decada")/10).cast("int") * 10)
dados_json = dados_json.withColumn("notaMedia", round("notaMedia", 1))

dados_movies = dados_csv.unionByName(dados_json)
dados_movies = dados_movies.dropDuplicates(["titulo"])
dados_movies = dados_movies.orderBy("titulo")

dados_movies = dados_movies.withColumn(
        "tempoMinutos",
        when(col("tempoMinutos") == r"\N", None).otherwise(col("tempoMinutos"))
)
dados_movies = dados_movies.withColumn("id", monotonically_increasing_id())

now = datetime.now()
dados_movies = dados_movies \
        .withColumn("ano", lit(now.year)) \
        .withColumn("mes", lit(now.month)) \
        .withColumn("dia", lit(now.day))
dados_movies.write.mode("overwrite").partitionBy("ano", "mes", "dia").format("parquet").save(target_path)
