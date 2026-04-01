from pyspark.sql import SparkSession
from pyspark.sql.functions import col, split, year, round, array_contains, when, monotonically_increasing_id, lit
from datetime import datetime


spark = SparkSession.builder.master("local[*]").appName("Create Trusted Series").getOrCreate()

source_json_file = args['S3_JSON_SERIES_PATH']
source_csv_file = args['S3_CSV_SERIES_PATH']
target_path = args['TARGET_PATH']

dados_json = spark.read.format("json").option("multiline", True).load(source_json_file)
dados_csv = spark.read.format("csv").option("header", True).option("sep", "|").load(source_csv_file)

dados_json = dados_json.drop("id", "original_name", "vote_count")
dados_json = dados_json.withColumnsRenamed({"genre_ids": "genero", "name": "titulo", "vote_average": "notaMedia", "first_air_date": "anoLancamento", "last_air_date": "anoTermino"})
dados_json = dados_json.withColumn("decada", (year("anoLancamento")/10).cast("int") * 10)
dados_json = dados_json.withColumn("anoLancamento", year("anoLancamento"))
dados_json = dados_json.withColumn(
        "anoTermino",
        when(col("anoTermino") == r"\N", None)
        .otherwise(year(col("anoTermino")))
)
dados_json = dados_json.withColumn("notaMedia", round("notaMedia", 1))

dados_csv = dados_csv.drop("id", "tituloOriginal", "tempoMinutos", "numeroVotos", "generoArtista", "personagem", "nomeArtista", "anoNascimento", "anoFalecimento", "profissao", "titulosMaisConhecidos")
dados_csv = dados_csv.withColumnsRenamed({"tituloPincipal": "titulo"})
dados_csv = dados_csv.dropDuplicates(["titulo"])
dados_csv = dados_csv.withColumn("genero", split("genero", ","))
dados_csv = dados_csv.filter(
        array_contains("genero", "Comedy")
        | array_contains("genero", "Animation")
)
dados_csv = dados_csv.withColumn("decada", (col("anoLancamento")/10).cast("int") * 10)
dados_csv = dados_csv.withColumn(
        "anoTermino",
        when(col("anoTermino") == r"\N", None)
        .otherwise(col("anoTermino"))
)
dados_csv = dados_csv.withColumn("notaMedia", round("notaMedia", 1))

dados_series = dados_csv.unionByName(dados_json)
dados_series = dados_series.dropDuplicates(["titulo"])
dados_series = dados_series.orderBy("titulo")

dados_series = dados_series.withColumn(
        "ativo", 
        when(col("anoTermino") == "NULL", None)
        .otherwise((col("anoTermino")-col("anoLancamento")+1).cast("int"))
)
dados_series = dados_series.drop("anoLancamento", "anoTermino")
dados_series = dados_series.withColumn("id", monotonically_increasing_id())

now = datetime.now()
dados_series = dados_series \
        .withColumn("ano", lit(now.year)) \
        .withColumn("mes", lit(now.month)) \
        .withColumn("dia", lit(now.day))
dados_series.write.mode("overwrite").partitionBy("ano", "mes", "dia").format("parquet").save(target_path)

