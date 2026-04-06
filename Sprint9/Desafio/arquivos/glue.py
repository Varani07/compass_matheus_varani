from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import col, when, lit, explode, row_number, desc


spark = SparkSession.builder.master("local[*]").appName("teste").getOrCreate()

source_movies = "Movies/"
source_series = "Series/"

df_series = spark.read.parquet(source_series)
df_movies = spark.read.parquet(source_movies)

df_movies = df_movies.withColumn("tipo", lit("movie"))
df_series = df_series.withColumn("tipo", lit("serie"))

df_movies = df_movies.withColumn("ativo", lit(None))
df_series = df_series.withColumn("tempoMinutos", lit(None))

df = df_series.unionByName(df_movies)
df = df.drop("dia", "mes", "ano")
df = df.withColumnsRenamed({"notaMedia": "nota_media", "tempoMinutos": "tempo_minutos", "id": "id_conteudo"})
df = df.where((col("decada").isNotNull()) | (col("tipo") != lit("serie")))
df = df.withColumn("decada", when(col("decada").isNull(), -1).otherwise(col("decada")))
window_spec_conteudo = Window.orderBy("tipo", "titulo")
df = df.withColumn("id_conteudo", row_number().over(window_spec_conteudo))

dim_decada = df.select("decada").distinct()
window_spec_decada = Window.orderBy("decada")
dim_decada = dim_decada.withColumn("id_decada", row_number().over(window_spec_decada))

df_exploded = df.withColumn("genero", explode(col("genero")))
dim_genero = df_exploded.select("genero").distinct()
window_spec_genero = Window.orderBy("genero")
dim_genero = dim_genero.withColumn("id_genero", row_number().over(window_spec_genero))
bridge_conteudo_genero = df_exploded.select("genero", "id_conteudo").join(dim_genero, on="genero", how="inner").select("id_conteudo", "id_genero")

fato_conteudo = df.join(dim_decada, on="decada", how="inner").select("id_conteudo", "id_decada", "nota_media")
dim_conteudo = df.select("id_conteudo", "titulo", "tipo", "tempo_minutos", "ativo")

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

fato_conteudo.createOrReplaceTempView("fato")
dim_conteudo.createOrReplaceTempView("conteudo")
dim_decada.createOrReplaceTempView("decada")
dim_genero.createOrReplaceTempView("genero")
bridge_conteudo_genero.createOrReplaceTempView("conteudo_genero")

relacao_duracao_nota_filmes_comedia = spark.sql("""
SELECT c.tempo_minutos, f.nota_media
FROM fato f
JOIN conteudo c ON f.id_conteudo = c.id_conteudo
JOIN conteudo_genero cg ON c.id_conteudo = cg.id_conteudo
JOIN genero g ON cg.id_genero = g.id_genero
WHERE c.tipo = 'movie' AND g.genero = 'Comedy' AND c.tempo_minutos IS NOT NULL 
ORDER BY c.tempo_minutos;                                                
""")

relacao_decada_nota_filmes_comedia_animacao = spark.sql("""
SELECT d.decada, f.nota_media
FROM fato f
JOIN conteudo c ON f.id_conteudo = c.id_conteudo
JOIN conteudo_genero cg ON c.id_conteudo = cg.id_conteudo
JOIN genero g ON cg.id_genero = g.id_genero
JOIN decada d ON f.id_decada = d.id_decada
WHERE (g.genero = 'Animation' OR g.genero = 'Comedy') AND c.tipo = 'movie' AND (d.decada != -1 AND f.nota_media IS NOT NULL)
ORDER BY d.decada;                                                  
""")

relacao_tempo_ativo_nota_series_comedia_animacao = spark.sql("""
SELECT c.ativo, f.nota_media
FROM fato f
JOIN conteudo c ON f.id_conteudo = c.id_conteudo
JOIN conteudo_genero cg ON c.id_conteudo = cg.id_conteudo
JOIN genero g ON cg.id_genero = g.id_genero
WHERE (g.genero = 'Animation' OR g.genero = 'Comedy') AND c.ativo IS NOT NULL AND c.tipo = 'serie'
ORDER BY c.ativo;                                                 
""")

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

