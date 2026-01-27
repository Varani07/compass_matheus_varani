# Desafio
Procurar por um arquivo `JSON` ou `CSV` no portal de dados públicos do Governo Brasileiro e a partir do arquivo escolhido realizar uma série etapas com as seguintes técnologias: `Python (libs: boto3, pandas)` e `AWS S3`.

## Sumário
- [Etapa 1](#et1)
- [Etapa 2](#et2)
    - [a](#analise-1)
    - [b](#analise-2)
    - [c](#analise-3)
- [Etapa 3](#et3)

## <a name="et1">Etapa 1</a>
- Analisar o conjunto de dados escolhido;
- Definir 3 questionamentos ou análises que pretende trazer com os dados escolhidos;
- A partir de um script Python, carregar o arquivo para um bucket no AWS S3 utilizando a biblioteca boto3.<br><br>

Escolhi [este](/Sprint6/Desafio/arquivos/comprasGOV_original.csv) arquivo CSV (Compras Públicas do Governo Federal, Registros novos e/ou alterados em 2026-01-25) no [site](http://dados.gov.br) do Governo. [Neste](/Sprint6/Desafio/arquivos/organizando_dados.ipynb) arquivo (Jupyter Notebook) organizei o Dataset fazendo uso do argumento `usecols` em sua leitura, gerei um novo [CSV](/Sprint6/Desafio/arquivos/comprasGOV_modificado.csv) com `to_csv()` e enviei o mesmo para o bucket.<br><br>

- Análises escolhidas:
    - `5 Itens mais caros, a mediana e média de todas as contratações efetivadas`
        - Função de conversão: **to_numeric**;
        - Função de agregação: **mean, median**.
    - `Itens Homologados que foram comprados em 2025`
        - Função de data: **to_datetime, dt.year**
        - Cláusula que filtra dados usando ao menos dois operadores lógicos: **notna() & ==**
    - `Adição da coluna categoria_item`
        - Função de string: **str.contains**
        - Função condicional: **df.loc[df['col'].str.contains('string1|string2', case=False, na=False), 'nova_col'] = 'novo_valor'**

## <a name="et2">Etapa 2</a>
- Executando Análises;
- [Arquivo que as contém.](/Sprint6/Desafio/arquivos/analises.ipynb)

### <a name="analise-1">a</a>
### <a name="analise-2">b</a>
### <a name="analise-3">c</a>

## <a name="et3">Etapa 3</a>