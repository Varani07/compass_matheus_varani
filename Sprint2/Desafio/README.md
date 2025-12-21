# Desafio
O desafio proposto para esta Sprint pede para que uma tabela seja normalizada, então aplicando a modelagem relacional e posteriormente a dimensional.

## Normalizando a tabela
Primeiramente fiz uso [deste](/Sprint2/Desafio/arquivos/organizando_dados.sql) arquivo para organizar os dados fornecidos de uma maneira coesa que respeitasse as boas práticas de normalização.<br><br>Separei as informações de cada entidade em grupos de forma a fazer sentido e denominei seus respectivos links (chave estrangeira).

## Modelo Relacional
Após a normalização foi simples colocar a modelagem relacional em prática, no ***Dbeaver*** gerei as tabelas necessárias e as populei com os dados fornecidos. Comandos utilizados durante essa etapa se encontram [aqui](/Sprint2/Desafio/arquivos/etapa1.sql).

![img_mod_relacional](/Sprint2/Evidencias/desafio/etapa1/modelagem_relacional.png)

## Modelo Dimensional
Para exibir o modelo dimensional fiz o uso de ***views***, conforme sugerido. Foi bem simples de gerar, [aqui](/Sprint2/Desafio/arquivos/etapa2.sql) se encontra o código utilizado.<br><br>Apenas necessitei centralizar as informações de cada entidade, evitando então a dispersão de informações. Apesar da redundância de algumas colunas como ***nome*** e ***estado*** presentes tanto na tabela do cliente quanto na do vendedor, acredito que esta seja justamente a proposta da modelagem dimensional, diminuir a lógica necessária em pesquisas no banco de dados e agilizar a busca.

![img_mod_dimensional](/Sprint2/Evidencias/desafio/etapa2/modelagem_dimensional.png)