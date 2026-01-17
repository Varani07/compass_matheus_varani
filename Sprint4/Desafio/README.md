# Desafio
Foi proposto que fosse realizado uma série de atividades em um arquivo .csv contendo dados de aplicativos utilizando as bibliotecas ***pandas*** e ***matplotlib***.

## Sumário
- [Etapa 1](#etapa-1)
- [Etapa 2](#etapa-2)
- [Etapa 3](#etapa-3)
- [Etapa 4](#etapa-4)
- [Etapa 5](#etapa-5)
- [Etapa 6](#etapa-6)
- [Etapa 7](#etapa-7)
    - [Parte 1](#etapa-7_parte-1)
    - [Parte 2](#etapa-7_parte-2)
- [Etapa 8](#etapa-8)
    - [Parte 1](#etapa-8_parte-1)
    - [Parte 2](#etapa-8_parte-2)

## <a name="etapa-1">Etapa 1</a>
- Remover as linhas duplicadas. <br><br>

Para isso, levando em consideração que haviam linhas idênticas, porém com a Coluna 'Reviews' diferente, foi necessário converter para número a coluna 'Reviews' e então ordenar de forma decrescente, mantendo assim a informação mais relevante para cada aplicativo. <br><br>

Após isso utilizei drop_duplicates para remover as linhas duplicadas pelo nome do aplicativo ('App'). <br><br>

Nota-se também a utilização do argumento errors='coerce', para lidar com possíveis valores não numéricos na coluna 'Reviews'.

```python
apps['Reviews'] = pd.to_numeric(
    apps['Reviews'],
    errors='coerce'
)
apps = apps.sort_values('Reviews', ascending=False)
apps = apps.drop_duplicates(subset='App')
```

## <a name="etapa-2">Etapa 2</a>
- Faça um gráfico com barras contendo os top 5 apps por número de instalações. <br><br>

Defini o número de aplicativos a ser exibido em uma variável, assim facilitando possíveis alterações futuras. Nomeei os eixos e o título do gráfico para melhor entendimento do que está sendo exibido. Foi utilizado apps_por_installs, que foi um ordenação criada previamente para facilitar a criação desse gráfico.

```python
num_apps = 5
plt.barh(apps_por_installs['App'].head(num_apps), apps_por_installs['Installs'].head(num_apps))
plt.xlabel('Quantia instalada')
plt.ylabel('Aplicativos')
plt.title(f'Top {num_apps} Apps Mais Instalados')
plt.show()
```
![evidencia_etapa2](/Sprint4/Evidencias/desafio/etapa_2.png)

## <a name="etapa-3">Etapa 3</a>
- Faça um gráfico de pizza mostrando as categorias de apps existentes no dataset de acordo com a frequência em que aparecem. <br><br>

Fiz uso do value_counts() que retorna as categorias se acessado com .index e suas respectivas quantidades com .values. Formatando o autopct para exibir apenas uma casa decimal.

```python
contagem = apps['Category'].value_counts().head(5)
plt.pie(
    contagem.values,
    labels=contagem.index,
    autopct=lambda valor: f'{valor:.1f}%',
    startangle=90
)
plt.title('Categorias mais frequentes')
plt.show()
```
![evidencia_etapa3](/Sprint4/Evidencias/desafio/etapa_3.png)

## <a name="etapa-4">Etapa 4</a>
- Mostre qual o app mais caro existente no dataset. <br><br>

A partir de uma ordenação por preço decrescente, selecionei a primeira linha e formatei a resposta para exibir o nome do aplicativo e seu preço.

```python
app_mais_caro = app_por_preco.head(1)
print(f"O app mais caro presente no dataset é {app_mais_caro['App'].iloc[0]}, custando US${app_mais_caro['Price'].iloc[0]}.")
```

## <a name="etapa-5">Etapa 5</a>
- Mostre quantos apps são classificados como 'Mature 17+'. <br><br>

Sem grandes complicações, filtrei e com len() consegui o número de linhas presente no resultado.

```python
apps_mais_17 = apps.loc[apps['Content Rating'] == 'Mature 17+']
print(f"{len(apps_mais_17)} apps no dataset são classificados como 'Mature 17+'.")
```

## <a name="etapa-6">Etapa 6</a>
- Mostre o top 10 apps por número de reviews bem como o respectivo número de reviews. Ordene a lista de forma decrescente por número de reviews. <br><br>

Com zip() juntei as duas colunas que continham as informações necessárias e com enumerate() criei uma numeração para cada linha exibida.

```python
num_apps = 10
print('Top 10 apps por número de reviews\n')
for i, row in enumerate(zip(apps['App'].head(num_apps), apps['Reviews'].head(num_apps)), 1):
    print(f"{i}. {row[0]}, {row[1]} reviews")
```

## <a name="etapa-7">Etapa 7</a>
- Crie pelo menos mais 2 cálculos sobre o dataset e apresente um em formato de lista e outro em formato de valor. <br><br>

### <a name="etapa-7_parte-1">Parte 1</a> 
- Top 10 Gêneros mais frequêntes em conjunto com seu respectivo app mais bem avaliado. <br><br>

Como fiz uso do .items() junto com enumerate(), precisei separar: index, (chave, valor) na iteração do for loop. <br>
Para utilizar duas condições no filtro, precisei separar ambas com parenteses e o operador &. Com .notna() evitei possíveis problemas com valores nulos na coluna 'Rating'. 

```python
num_generos = 10
frequencia_generos = apps['Genres'].value_counts().head(num_generos)
print(f"Top {num_generos} gêneros mais frequentes no dataset em conjunto com seu respectivo app mais bem avaliado\n")
print('Gênero | Frequencia | App')
for i, (genre, count) in enumerate(frequencia_generos.items(), 1):
    best_rating_app = apps_por_rating[
        (apps_por_rating['Genres'] == genre)
        & (apps_por_rating['Rating'].notna())
    ].head(1)
    print(f"{i}. {genre}, {count}, {best_rating_app['App'].iloc[0]}")
```

### <a name="etapa-7_parte-2">Parte 2</a>
- App gratuito mais bem avaliado. <br><br>

Reutilizei a ordenação por rating e filtrei para que o resultado contemplasse apenas aplicativos gratuitos.

```python
best_free_app = apps_por_rating.loc[apps_por_rating['Type'] == 'Free'].head(1)
print(f"O aplicativo gratuito mais bem avaliado é o '{best_free_app['App'].iloc[0]}', com uma avaliação de {best_free_app['Rating'].iloc[0]} estrelas.")
```

## <a name="etapa-8">Etapa 8</a>
- Crie pelo menos outras 2 formas gráficas de exibição dos indicadores acima utilizando a biblioteca matplotlib. <br><br>

### <a name="etapa-8_parte-1">Parte 1</a>
- Gráfico Boxplot evidenciando as avaliações dos aplicativos que pertencem aos 10 gêneros mais frequentes no dataset. <br><br>

Realmente a parte mais divertida do desafio. Criar este gráfico foi relativamente simples, reutilizando a variável frequencia_generos e filtrando com ***isin()*** para conter apenas os gêneros desejados. A parte complexa foi entender o gráfico gerado, o que levou algumas vídeo aulas, todavia foi um aprendizado muito rico e importante. O Gráfico Boxplot é extremamente útil para entender a distribuição dos dados.

```python
apps_filtrados = apps_por_rating[apps_por_rating['Genres'].isin(frequencia_generos.index)]
apps_filtrados.boxplot(column='Rating', by='Genres', rot=45)
plt.title('Distribuição das avaliações por gênero')
plt.suptitle('')
plt.xlabel('Gêneros')
plt.ylabel('Avaliações')
plt.show()
```
![evidencia_etapa8_parte1](/Sprint4/Evidencias/desafio/etapa_8_parte_1.png)

### <a name="etapa-8_parte-2">Parte 2</a>
- Comparação entre as avaliações de aplicativos pagos e gratuitos. <br><br>

Com filtros para cada tipo de aplicativo, utilizei o value_count() para contar a quantia de apps por avaliação e com sort_index() organizei para que o gráfico fosse exibido da forma correta. Com um for loop evitei a repetição de código, .grid(True) para facilitar a visualização do gráfico e .legend() para identificar cada linha exibida.

```python
gratuitos_por_rating = apps_gratuitos['Rating'].value_counts().sort_index(), 'Gratuitos'
pagos_por_rating = apps_pagos['Rating'].value_counts().sort_index(), 'Pagos'

for tipo in [gratuitos_por_rating, pagos_por_rating]:
    plt.plot(
        tipo[0].index,
        tipo[0].values,
        label=tipo[1],
        marker='o'
    )
plt.title('Comparativo de aplicativos gratuitos/pagos por avaliação')
plt.xlabel('Rating')
plt.ylabel('Quantidade De Aplicativos')
plt.grid(True)
plt.legend()
plt.show()
```
![evidencia_etapa8_parte2](/Sprint4/Evidencias/desafio/etapa_8_parte_2.png)