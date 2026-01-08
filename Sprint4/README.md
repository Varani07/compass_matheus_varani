# Resumo

> ***SQL Para Análise de Dados***
- Instalar e configurar o pgAdmin/PostgreSQL
- Visão geral sobre o pgAdmin
- Revisei conhecimentos sobre: Select, Order By, Where, Limit, Join, Operadores Aritméticos e de comparação.
- Aprendi a utilizar: Having, Subqueries, Union, Distinct, Operadores Lógicos e Funções de Agregação.

Aprofundei em muito meu conhecimento com as aulas precisas e claras da instrutora, aprendendo sobre conversão de unidades e tratamento de dados com exemplos práticos e realistas.

> ***Data & Analytics - PB - AWS (A partir da Seção 9 até a 16)***
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

___

# Evidências
Evidências dos exercícios realizados na sprint contendo um breve parecer:
- <a name="e01">Exercício 1<a/>
    - Pode-se facilmente chegar no resultado pedido ao utilizar o operador relacional maior ou igual a na data ***2015-01-01***, após isso apenas ordenar pelo id e apresentar as colunas pedidas.
    > ![evidenvcia_e01](/Sprint2/Evidencias/biblioteca/e01.png)

- <a name="e02">Exercício 2<a/>
    - Utilizei Limit para buscar apenas a quantidade pedida na questão e ordenei o valor por ordem decrescente assim então conseguindo os 10 livros mais caros. 
    > ![evidenvcia_e02](/Sprint2/Evidencias/biblioteca/e02.png)

- <a name="e03">Exercício 3<a/>
    - Neste exercício utilizei de uma ***subquerie no select***, o que não é aconselhavel por não ser uma estratégia que escala bem ao decorrer do aumento dos dados presentes no banco. Apesar disso obtive com sucesso o retorno esperado. 
    > ![evidenvcia_e03](/Sprint2/Evidencias/biblioteca/e03.png)

- <a name="e04">Exercício 4<a/>
    - Verifiquei a resposta esperada e a única necessidade da troca do 'Á' por 'A' era na ordem, utilizar um replace no order by resolveu o problema.
    > ![evidenvcia_e04](/Sprint2/Evidencias/biblioteca/e04.png)

- <a name="e05">Exercício 5<a/>
    - Utilizei o ***with*** para gerar uma tabela temporária contendo o id da editora e se ela é ou não de um estado que eu gostaria de ter no retorno, futuramente então a colocando em um join para então poder usar a coluna ***regiao_certa no where***.
    > ![evidenvcia_e05](/Sprint2/Evidencias/biblioteca/e05.png)

- <a name="e06">Exercício 6<a/>
    - Fiz uso de uma subquerie para conseguir a quantidades de livros publicados por autor com limit e order by para mostrar apenas o que tem a maior quantidade de publicações.
    > ![evidenvcia_e06](/Sprint2/Evidencias/biblioteca/e06.png)

- <a name="e07">Exercício 7<a/>
    - Acredito que poderia ter solucionado este exercício com o ***having***, mas fui ter mais domínio acerca dele só na segunda parte das atividades.
    > ![evidenvcia_e07](/Sprint2/Evidencias/biblioteca/e07.png)

- <a name="e08">Exercício 8<a/>
    - Outro momento em que acredito poder ter utilizado o having. Utilizei uma subquerie para retornar qual vendedor teve o maior número de vendas concluídas.
    > ![evidenvcia_e08](/Sprint2/Evidencias/loja/e08.png)

- <a name="e09">Exercício 9<a/>
    - Utilizando de várias condições dentro da subquerie no order by cheguei na resolução da questão.
    > ![evidenvcia_e09](/Sprint2/Evidencias/loja/e09.png)

- <a name="e10">Exercício 10<a/>
    - Demorei um pouco neste, pois esqueci de colocar a condição do código do vendedor em uma das subqueries, após isso concluí sem grandes dificuldades.
    > ![evidenvcia_e10](/Sprint2/Evidencias/loja/e10.png)

- <a name="e11">Exercício 11<a/>
    - Nomeei o retorno da subquerie como gasto e ordenei por este resultado de forma decrescente para conseguir o maior gasto.
    > ![evidenvcia_e11](/Sprint2/Evidencias/loja/e11.png)

- <a name="e12">Exercício 12<a/>
    - Com certeza um dos maiores códigos sql que fiz e também meu primeiro uso do having. Realizei os join's necessários e agrupei, necessário caso esteja utilizando de funções de agregação.
    > ![evidenvcia_e12](/Sprint2/Evidencias/loja/e12.png)

- <a name="e13">Exercício 13<a/>
    - Mesma lógica do exercício anterior na questão do agrupamento por conta da função de agregação, também utilizando o ***where*** para impor uma condição e filtrar a busca. 
    > ![evidenvcia_e13](/Sprint2/Evidencias/loja/e13.png)

- <a name="e14">Exercício 14<a/>
    - Acredito que tenha sido minha primeira vez utilizando a função de agregação ***avg*** que retorna uma média da coluna(s) selecionada, neste caso foi o gasto médio por estado.
    > ![evidenvcia_e14](/Sprint2/Evidencias/loja/e14.png)

- <a name="e15">Exercício 15<a/>
    - Talvez o código mais simples dentre todos os exercícios, só precisei realizar um select na tabela para entender a coluna ***deletado*** e após isso não tive problemas.
    > ![evidenvcia_e15](/Sprint2/Evidencias/loja/e15.png)

- <a name="e16">Exercício 16<a/>
    - Utilizei a função round para arredondar o retorno como foi pedido no enunciado e ordenar da forma solicitada.
    > ![evidenvcia_e16](/Sprint2/Evidencias/loja/e16.png)