# Resumo

> ***SQL Para Análise de Dados***
- Instalar e configurar o pgAdmin/PostgreSQL
- Visão geral sobre o pgAdmin
- Revisei conhecimentos sobre: Select, Order By, Where, Limit, Join, Operadores Aritméticos e de comparação.
- Aprendi a utilizar: Having, Subqueries, Union, Distinct, Operadores Lógicos e Funções de Agregação.

Aprofundei em muito meu conhecimento com as aulas precisas e claras da instrutora, aprendendo sobre conversão de unidades e tratamento de dados com exemplos práticos e realistas.

> ***Data & Analytics - PB - AWS - 2/10 (A partir da Seção 9 até a 16)***
- Concluindo as atividades propostas consegui então concretizar o conhecimento adquirido no curso de SQL. 
- Aprendi também sobre como exportar os dados vindos de uma pesquisa com *select* definindo o separador, bem como a utilizar o *DBeaver* como ferramenta para atingir o objetivo proposto pelo desafio da Sprint 2.

___

# Desafio
Pasta contendo arquivos e README.md referente ao desafio proposto:
- [Pasta do desafio](/Sprint2/Desafio/)
- [README.md do desafio](/Sprint2/Desafio/README.md)

___

# Exercícios
Lista dos exercícios realizados, contendo um link para a solução e outro que irá levar a sua devida evidência.

## Biblioteca
- Exercício 1:
    - [Script .sql contendo resposta](/Sprint2/Exercicios/biblioteca/e01/e01.sql)
    - [Evidência](#e01)

- Exercício 2:
    - [Script .sql contendo resposta](/Sprint2/Exercicios/biblioteca/e02/e02.sql)
    - [Evidência](#e02)

- Exercício 3:
    - [Script .sql contendo resposta](/Sprint2/Exercicios/biblioteca/e03/e03.sql)
    - [Evidência](#e03)

- Exercício 4:
    - [Script .sql contendo resposta](/Sprint2/Exercicios/biblioteca/e04/e04.sql)
    - [Evidência](#e04)

- Exercício 5:
    - [Script .sql contendo resposta](/Sprint2/Exercicios/biblioteca/e05/e05.sql)
    - [Evidência](#e05)

- Exercício 6:
    - [Script .sql contendo resposta](/Sprint2/Exercicios/biblioteca/e06/e06.sql)
    - [Evidência](#e06)

- Exercício 7:
    - [Script .sql contendo resposta](/Sprint2/Exercicios/biblioteca/e07/e07.sql)
    - [Evidência](#e07)

## Loja
- Exercício 8:
    - [Script .sql contendo resposta](/Sprint2/Exercicios/loja/e08/e08.sql)
    - [Evidência](#e08)

- Exercício 9:
    - [Script .sql contendo resposta](/Sprint2/Exercicios/loja/e09/e09.sql)
    - [Evidência](#e09)

- Exercício 10:
    - [Script .sql contendo resposta](/Sprint2/Exercicios/loja/e10/e10.sql)
    - [Evidência](#e10)

- Exercício 11:
    - [Script .sql contendo resposta](/Sprint2/Exercicios/loja/e11/e11.sql)
    - [Evidência](#e11)

- Exercício 12:
    - [Script .sql contendo resposta](/Sprint2/Exercicios/loja/e12/e12.sql)
    - [Evidência](#e12)

- Exercício 13:
    - [Script .sql contendo resposta](/Sprint2/Exercicios/loja/e13/e13.sql)
    - [Evidência](#e13)

- Exercício 14:
    - [Script .sql contendo resposta](/Sprint2/Exercicios/loja/e14/e14.sql)
    - [Evidência](#e14)

- Exercício 15:
    - [Script .sql contendo resposta](/Sprint2/Exercicios/loja/e15/e15.sql)
    - [Evidência](#e15)

- Exercício 16:
    - [Script .sql contendo resposta](/Sprint2/Exercicios/loja/e16/e16.sql)
    - [Evidência](#e16)

## Exportação de Dados
- Etapa 1:
    - [Script .sql contendo resposta](/Sprint2/Exercicios/exportacao_dados/etapa_1/etapa1.sql)
    - [Evidência](#etapa_1)

- Etapa 2:
    - [Script .sql contendo resposta](/Sprint2/Exercicios/exportacao_dados/etapa_2/etapa2.sql)
    - [Evidência](#etapa_2)
___

# Evidências
Evidências dos exercícios realizados na sprint contendo um breve parecer:

## Biblioteca
- <a name="e01">Exercício 1</a>
    - Pode-se facilmente chegar no resultado pedido ao utilizar o operador relacional maior ou igual a na data ***2015-01-01***, após isso apenas ordenar pelo id e apresentar as colunas pedidas. <br><br>
    > ![evidencia_e01](/Sprint2/Evidencias/biblioteca/e01.png)

- <a name="e02">Exercício 2</a>
    - Utilizei Limit para buscar apenas a quantidade pedida na questão e ordenei o valor por ordem decrescente assim então conseguindo os 10 livros mais caros. <br><br> 
    > ![evidencia_e02](/Sprint2/Evidencias/biblioteca/e02.png)

- <a name="e03">Exercício 3</a>
    - Neste exercício utilizei de uma ***subquerie no select***, o que não é aconselhavel por não ser uma estratégia que escala bem ao decorrer do aumento dos dados presentes no banco. Apesar disso obtive com sucesso o retorno esperado. <br><br>
    > ![evidencia_e03](/Sprint2/Evidencias/biblioteca/e03.png)

- <a name="e04">Exercício 4</a>
    - Verifiquei a resposta esperada e a única necessidade da troca do 'Á' por 'A' era na ordem, utilizar um replace no order by resolveu o problema. <br><br>
    > ![evidencia_e04](/Sprint2/Evidencias/biblioteca/e04.png)

- <a name="e05">Exercício 5</a>
    - Utilizei o ***with*** para gerar uma tabela temporária contendo o id da editora e se ela é ou não de um estado que eu gostaria de ter no retorno, futuramente então a colocando em um join para então poder usar a coluna ***regiao_certa no where***. <br><br>
    > ![evidencia_e05](/Sprint2/Evidencias/biblioteca/e05.png)

- <a name="e06">Exercício 6</a>
    - Fiz uso de uma subquerie para conseguir a quantidades de livros publicados por autor com limit e order by para mostrar apenas o que tem a maior quantidade de publicações. <br><br>
    > ![evidencia_e06](/Sprint2/Evidencias/biblioteca/e06.png)

- <a name="e07">Exercício 7</a>
    - Acredito que poderia ter solucionado este exercício com o ***having***, mas fui ter mais domínio acerca dele só na segunda parte das atividades. <br><br>
    > ![evidencia_e07](/Sprint2/Evidencias/biblioteca/e07.png)

## Loja
- <a name="e08">Exercício 8</a>
    - Outro momento em que acredito poder ter utilizado o having. Utilizei uma subquerie para retornar qual vendedor teve o maior número de vendas concluídas. <br><br>
    > ![evidencia_e08](/Sprint2/Evidencias/loja/e08.png)

- <a name="e09">Exercício 9</a>
    - Utilizando de várias condições dentro da subquerie no order by cheguei na resolução da questão. <br><br>
    > ![evidencia_e09](/Sprint2/Evidencias/loja/e09.png)

- <a name="e10">Exercício 10</a>
    - Demorei um pouco neste, pois esqueci de colocar a condição do código do vendedor em uma das subqueries, após isso concluí sem grandes dificuldades. <br><br>
    > ![evidencia_e10](/Sprint2/Evidencias/loja/e10.png)

- <a name="e11">Exercício 11</a>
    - Nomeei o retorno da subquerie como gasto e ordenei por este resultado de forma decrescente para conseguir o maior gasto. <br><br>
    > ![evidencia_e11](/Sprint2/Evidencias/loja/e11.png)

- <a name="e12">Exercício 12</a>
    - Com certeza um dos maiores códigos sql que fiz e também meu primeiro uso do having. Realizei os join's necessários e agrupei, necessário caso esteja utilizando de funções de agregação. <br><br>
    > ![evidencia_e12](/Sprint2/Evidencias/loja/e12.png)

- <a name="e13">Exercício 13</a>
    - Mesma lógica do exercício anterior na questão do agrupamento por conta da função de agregação, também utilizando o ***where*** para impor uma condição e filtrar a busca. <br><br>
    > ![evidencia_e13](/Sprint2/Evidencias/loja/e13.png)

- <a name="e14">Exercício 14</a>
    - Acredito que tenha sido minha primeira vez utilizando a função de agregação ***avg*** que retorna uma média da coluna(s) selecionada, neste caso foi o gasto médio por estado. <br><br>
    > ![evidencia_e14](/Sprint2/Evidencias/loja/e14.png)

- <a name="e15">Exercício 15</a>
    - Talvez o código mais simples dentre todos os exercícios, só precisei realizar um select na tabela para entender a coluna ***deletado*** e após isso não tive problemas. <br><br>
    > ![evidencia_e15](/Sprint2/Evidencias/loja/e15.png)

- <a name="e16">Exercício 16</a>
    - Utilizei a função round para arredondar o retorno como foi pedido no enunciado e ordenar da forma solicitada. <br><br>
    > ![evidencia_e16](/Sprint2/Evidencias/loja/e16.png)

## Exportação de Dados
- <a name="etapa_1">Etapa 1</a>
    - Fazendo uso do comando sqlite3 direto no terminal consegui exportar o resultado do select para um arquivo .csv, apenas definindo o separador como ponto e vírgula. <br><br>
    > [Evidência - Etapa 1](/Sprint2/Evidencias/exportacao_dados/etapa1.csv)

- <a name="etapa_2">Etapa 2</a>
    - Mesma lógica da etapa 1, apenas alterando o separador para |. 
    <br><br>
    > [Evidência - Etapa 2](/Sprint2/Evidencias/exportacao_dados/etapa2.csv)