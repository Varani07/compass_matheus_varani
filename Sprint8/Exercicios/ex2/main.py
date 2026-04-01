from pyspark.sql import SparkSession
from pyspark import SparkContext
from random import choice
from pyspark.sql.functions import when, rand, expr, col


spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()
df_nomes = spark.read.csv("nomes_aleatorios.txt")
df_nomes.show(5)

df_nomes.printSchema()
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
df_nomes.show(10)

df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when(rand() < 0.33, "Fundamental")
    .when(rand() < 0.66, "Medio")
    .otherwise("Superior")
    )

paises = ["Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Equador", "Guiana", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela", "Guiana Francesa"]
paises_sql = ",".join(f"'{item}'" for item in paises)
df_nomes = df_nomes.withColumn(
    "Pais",
    expr(f"element_at(array({paises_sql}), int(rand()*{len(paises)})+1)")
)

anos = [ano for ano in range(1945, 2011)]
anos_sql = ",".join(str(ano) for ano in anos)
df_nomes = df_nomes.withColumn(
    "AnoNascimento",
    expr(f"element_at(array({anos_sql}), int(rand()*{len(anos)})+1)")
)

df_select = df_nomes.select("*").where(col("AnoNascimento") >= 2000)
df_select.show(10)

df_nomes.createOrReplaceTempView("pessoas")
spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000").show()

print(
    df_nomes.filter(
        (col("AnoNascimento") >= 1980)
        & (col("AnoNascimento") <= 1994)
    ).count()
)

spark.sql("SELECT COUNT(*) FROM pessoas WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994").show()

df_resultados = spark.sql("""
                          SELECT 
                                Pais,
                                CASE
                                        WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
                                        WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geracao X'
                                        WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
                                        WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geracao Z'
                                END AS Geracao,
                                COUNT(*) AS Quantidade
                          FROM
                                pessoas
                          GROUP BY
                                Pais,
                                Geracao
                          ORDER BY
                                Pais,
                                Geracao,
                                Quantidade
""")
df_resultados.show(df_resultados.count())