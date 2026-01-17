# Resumo

> ***Data & Analytics - PB - AWS - 5/10 (Seção 6)***
Percebi que meu curso não estava filtrado, contém apenas uma breve instrodução do que será visto na Sprint. Mas como já havia lido um pouco do conteúdo e achei interessante, vou deixar abaixo.

- 4 principais módulos do Hadoop:
    1. Hadoop Distributed File System (HDFS);
    2. Yet Another Resource Negotiator (YARN);
    3. MapReduce;
    4. Hadoop Common.

- 5 processos necessários para que o Hadoop funcione:
    1. NameNode;
    2. DataNode;
    3. SecondaryNameNode;
    4. JobTracker;
    5. TaskTracker.

    MapReduce: NameNode, DataNode e SecondaryNameNode.
    HDFS: JobTracker e TaskTracker.

> ***Docker para Desenvolvedores - com Docker Swarm e Kubernetes (Seção 1 até 8, 10 e 12)***
- Instalação das seguintes ferramentas: Docker Desktop, Kubernetes, Minikube e Cmder.
- Docker:
    1. Baixar, Rodar, Montar e Gerenciar ***Imagens***, inclusive a enviar para o Docker Hub.
    2. Comandos para monitoramento de ***Containers***.
    3. Diversas ***flags*** aplicaveis em comandos.
    4. Gerenciar containers.
    5. Montar um ***Dockerfile***, precisei pesquisar por fora para consolidar os conhecimentos acerca da criação deste arquivo.
    6. Criar um ***Volume*** anônimo e nomeado, bem como utilizar o bind mount para sincronia do projeto.
    7. Gerar e Gerenciar uma ***Network*** e seus possíveis tipos.
    8. Como montar e aplicar o ***docker-compose*** para gerenciar diversos containers em conjunto.
- Docker Swarm:
    1. Utilizar os serviços da AWS para conseguir gerar Nodes.
    2. Comandos para configuração do ***swarm*** nas máquinas.
    3. Gerenciar e Monitorar nodes workers apartir do node manager.
    4. Gerenciar Serviços e Escalar o projeto para os demais Nodes.
    5. Criar uma ***Network***.
    6. Utilizar: ```ServerAliveInterval 50``` em  ```vim ~/.ssh/config``` para evitar a desconexão do servidor.
- Kubernetes:
    1. Abrir o Dashboard apartir do ***Minikube***.
    2. Gerenciar ***Deployments***, ***Pods*** e ***Services***.
    3. Escalar o projeto e monitorar as ***replicas***.
    4. Utilizar de um arquivo ```.yaml``` para configurar o projeto e o utilizar para rodar e atualizar todos os ***pods*** de forma prática e rápida.
    5. Retornar a versão anterior se necessário com o comando ```kubectl rollout undo deployment/<nome>```.

> ***Python - REGEX***
- Com o vídeo pude aprender o básico do básico sobre usos da biblioteca ***re***.
- Consolidei o conhecimento tentando criar padrões para endereços de email e cpf, corrigindo meus erros e aprendendo com o ***ChatGPT***, sempre perguntando o porque das coisas, tentando ao máximo entender para poder aplicar futuramente. Após fazer uso da IA, sempre testando no ***python*** da minha máquina para ter certeza dos resultados.
- Assisti a outros vídeos por fora, pois achei o assunto muito interessante e queria aprofundar meu conhecimento.
- Resultado para os padrões previamente ditos: ```r'(\d{3}\.){2}\d{3}-\d{2}' (cpf)```, ```r'^(?![._-])[\w.-]+(?<![._-])@gmail\.com(\.br)?$' (email)```. <br><br>
    ```
    1. "r" Antes da string é necessário para o Python não interpretar escapes.
    2. "\d" Utilizado para apontar um número de 0 até 9.
    3. "{numero}" Indica o número de vezes que a expressão a esquerda aparece.
    4. "(...)" Agrupa padrões.
    5. "\." Necessário fora de [] pois o . sozinho simboliza qualquer caracter.
    6. "^" Fora de [] simboliza o início da string.
    7. "(?!...)" Nega o que vem à frente.
    8. "(?<!...)" Nega o que vem antes.
    9. "[...]" Conjunto de valores.
    10. "-" Precisa estar no início ou fim do conjunto para ser tratado como literal, também pode-se usar: "\-".
    11. "\w" Valor alfanumérico ou _.
    12. "+" Ocorre pelo menos uma ou mais vezes.
    13. "$" Representa o fim da string.
    ```

___

# Desafio
Pasta contendo arquivos e README.md referente ao desafio proposto:
- [Pasta do desafio](/Sprint5/Desafio/)
- [README.md do desafio](/Sprint5/Desafio/README.md)