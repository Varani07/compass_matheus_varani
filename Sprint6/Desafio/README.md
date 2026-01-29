# Desafio
Procurar por um arquivo `JSON` ou `CSV` no portal de dados públicos do Governo Brasileiro e a partir do arquivo escolhido realizar uma série etapas com as seguintes técnologias: `Python (libs: boto3, pandas)` e `AWS S3`.

**Aviso:** Algumas das explicações sobre códigos utilizados nas próximas etapas vão estar presentes tanto nos seus respectivos arquivos **ipynb** quanto neste **README**, gerando redundância porém também a independência de cada um.

## Sumário
- [Preparativos](#prep)
- [Etapa 1](#et1)
- [Etapa 2](#et2)
    - [5 Itens mais caros, a mediana e média de todas as contratações efetivadas](#analise-1)
    - [Itens Homologados que foram comprados em 2025](#analise-2)
    - [Adição da coluna categoria_item](#analise-3)
- [Etapa 3](#et3)

## <a name="prep">Preparativos</a>
- Criando Bucket para seguir com as próximas etapas.<br><br>
![Criando Bucket](/Sprint6/Evidencias/desafio/criando-bucket.png)
- As credênciais necessárias para a utilização da biblioteca **boto3** não necessitam ser utilizadas de forma explícita, ao carregar as variáveis do arquivo **.env** com `load_dotenv()` para o ambiente, a biblioteca as reconhece de forma automática.
- Utilizei este comando no **cloudshell** para receber as credênciais temporárias: `aws configure export-credentials --format env`, depois copiei o output e colei dentro do arquivo **.env**.

## <a name="et1">Etapa 1</a>
- Analisar o conjunto de dados escolhido;
- Definir 3 questionamentos ou análises que pretende trazer com os dados escolhidos;
- A partir de um script Python, carregar o arquivo para um bucket no AWS S3 utilizando a biblioteca boto3.<br><br>

Escolhi [este](/Sprint6/Desafio/arquivos/comprasGOV_original.csv) arquivo CSV (Compras Públicas do Governo Federal, Registros novos e/ou alterados em 2026-01-25) no [site](http://dados.gov.br) do Governo. [Neste](/Sprint6/Desafio/arquivos/organizando_dados.ipynb) arquivo (Jupyter Notebook) organizei o Dataset fazendo uso do argumento `usecols` em sua leitura e gerei um novo [CSV](/Sprint6/Desafio/arquivos/comprasGOV_modificado.csv) com `to_csv()`.<br><br>

### Análises escolhidas:
- `5 Itens mais caros, a mediana e média de todas as contratações efetivadas`
    - Função de conversão: **to_numeric**;
    - Função de agregação: **mean, median**.
- `Itens Homologados que foram comprados em 2025`
    - Função de data: **to_datetime, dt.year**
    - Cláusula que filtra dados usando ao menos dois operadores lógicos: **notna() & ==**
- `Adição da coluna categoria_item`
    - Função de string: **str.contains**
    - Função condicional: **df.loc[df['col'].str.contains('string1|string2', case=False, na=False), 'nova_col'] = 'novo_valor'**

### Carregando arquivo `comprasGOV_modificado.csv` para o bucket:

- `boto3.resource('s3')` cria um ponto de acesso para interagir com o serviço Amazon S3.
- `s3.Bucket('desafio-sprint-06')` gera um objeto para representar o bucket que desejamos gerenciar.
- `bucket.upload_file('comprasGOV_modificado.csv', 'comprasGOV.csv')` envia o arquivo para o bucket referenciado pelo objeto, o primeiro argumento simboliza o arquivo local, o segundo é como o arquivo será nomeado dentro do bucket.

```python
s3 = boto3.resource('s3')
bucket = s3.Bucket('desafio-sprint-06')
bucket.upload_file('comprasGOV_modificado.csv', 'comprasGOV.csv')
```

- Imagem do bucket após a execução do Script:<br><br>
![Bucket com csv](/Sprint6/Evidencias/desafio/bucket-primeiro-envio.png)

## <a name="et2">Etapa 2</a>
- Executando Análises.
- [Arquivo que as contém.](/Sprint6/Desafio/arquivos/analises.ipynb)
- Carregando arquivo a partir do Bucket:
    - `boto3.client('s3')` cria um objeto que permite fazer requisições diretas ao **AWS S3**.
    - `get_object` retorna um dicionário contendo informações sobre o arquivo presente no bucket indicado.
    - `obj['Body']` representa o conteúdo do arquivo.<br><br>
    ```python
    s3_get_bucket = boto3.client('s3')
    obj = s3_get_bucket.get_object(
        Bucket='desafio-sprint-06',
        Key='comprasGOV.csv'
    )

    df = pd.read_csv(obj['Body'])
    ```

### <a name="analise-1">5 Itens mais caros, a mediana e média de todas as contratações efetivadas</a>
- Manipulações utilizadas: Função de **conversão** e **agregação**.
- `copy()` cria uma cópia independente do DataFrame, foi necessário, pois apesar de tudo funcionar, em alguns momentos a biblioteca emitia avisos se uma repartição fosse utilizada com `df[:]`.
```python
analise_1 = df.copy()
```
- **Função de Conversão:**
    - Converte a coluna para valores numéricos.

    - `erros='coerce'` foi utilizado para evitar erros por conta de valores inválidos.
    ```python
    analise_1['valor_total_resultado'] = pd.to_numeric(
        analise_1['valor_total_resultado'],
        errors='coerce'
    )
    ```

- **Ordenando Dataset:**
    - Organizando o Dataset em ordem decrescente.
    ```python
    analise_1 = analise_1.sort_values('valor_total_resultado', ascending=False)
    ```

- **Função de Agregação:**
    - `mean()` e `median()` trazem respectivamente a média e mediana e `round()` formata o valor para aparecerem apenas duas casas decimais no resultado.
    ```python
    media = analise_1['valor_total_resultado'].mean()
    mediana = analise_1['valor_total_resultado'].median()
    print(f"Media: R${round(media, 2)}\nMediana: R${round(mediana, 2)}")
    ```
    - Output:
        ```
        Media: R$1939.11
        Mediana: R$1170.88
        ```

- **Filtrando Itens Mais Caros:**
    ```python
    analise_1 = analise_1.head(5)
    ```

### <a name="analise-2">Itens Homologados que foram comprados em 2025</a>
- Manipulações utilizadas: Função de **data** e **Cláusula que filtra dados usando ao menos dois operadores lógicos**.

- **Função de Data:**
    - Passamos o formato em que os valores na coluna se encontram com `format`.
    - A função `pd.to_datetime` converte o valor presente na coluna para o tipo **datetime**.
    - `dt.year` extrai apenas o ano do campo informado.
    ```python
    analise_2['ano_compra'] = pd.to_datetime(analise_2['ano_compra'], format="%Y")
    analise_2['ano_compra'] = analise_2['ano_compra'].dt.year
    ```

- **Cláusula que filtra dados usando ao menos dois operadores lógicos:**
    - `notna()` filtra valores não nulos.
    - Condições precisam estar entre parenteses (quando mais de uma) para que a avaliação ocorra corretamente.
    ```python
    analise_2 = analise_2.loc[
        (analise_2['ano_compra'] == 2025)
        & (analise_2['valor_total_resultado'].notna())
    ]
    ```

### <a name="analise-3">Adição da coluna categoria_item</a>
- Manipulações utilizadas: Função **condicional** e de **string**.

- **Inserindo coluna e atribuindo valor default:**
    ```python
    analise_3.loc[:,'categoria_item'] = "Outros"
    ```

- **Função de String:**
    - Criando uma máscara para simplificar, minimizando a quantia de código necessário para aplicar a função condicional.
    - `contains` verifica se o campo do item em uma coluna específica possuí os caracteres em evidencia.
    ```python
    mascara = analise_3['descricao_resumida'].str.contains
    ```

- **Função Condicional:**
    - Aplica a função de string estabelecida previamente em conjunto com a função condicional para, caso a condição seja identificada, então o valor da coluna é alterado.
    - Foi necessário colocar a categoria **Carnes** por último por conta do item **Carne 'Sal'gada**, que acabava caindo como **Grãos e Mercearia**. 
    ```python
    analise_3.loc[mascara("fruta|legum|verdura", case=False, na=False), 'categoria_item'] = "Hortifruti"
    analise_3.loc[mascara("leite|creme de leite|manteiga|iogurte", case=False, na=False), 'categoria_item'] = "Laticínios"
    analise_3.loc[mascara("arroz|feijão|café|farinha|macarrão|açúcar|sal|fermento", case=False, na=False), 'categoria_item'] = "Grãos e Mercearia"
    analise_3.loc[mascara("embutido|polpa|conserva", case=False, na=False), 'categoria_item'] = "Processados"
    analise_3.loc[mascara("carne|frango|ave|bovina|suína|peixe", case=False, na=False), 'categoria_item'] = "Carnes"
    ```

## <a name="et3">Etapa 3</a>
- Praticamente o mesmo código utilizado para subir [este](/Sprint6/Desafio/arquivos/comprasGOV_modificado.csv) primeiro arquivo para o Bucket, única diferença é que fiz uso de um **for loop** para salvar todos de forma dinâmica, evitando repetição de código.
```python
s3_send_to_bucket = boto3.resource('s3')
bucket = s3_send_to_bucket.Bucket('desafio-sprint-06')
for num in range(1, 4):
    bucket.upload_file(f'analise-{num}.csv', f'analise-{num}.csv')
```
- Imagem do Bucket após a inclusão dos arquivos resultantes das análises:<br><br>
    ![Bucket Final](/Sprint6/Evidencias/desafio/bucket-segundo-envio.png)