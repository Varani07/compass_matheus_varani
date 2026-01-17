# Desafio
O desafio aborda alguns conhecimentos adquiridos no decorrer da Sprint a respeito de ***Docker***.

- [Etapa 1](#etapa-1)
- [Etapa 2](#etapa-2)
- [Etapa 3](#etapa-3)
- [Etapa 3 - Versão 2](#etapa-3-v2)
- [Extra](#extra)

## <a name="etapa-1">Etapa 1</a>
- Construindo uma imagem a partir do [Dockerfile](/Sprint5/Desafio/arquivos/etapa-1/Dockerfile)
    ![build](/Sprint5/Evidencias/desafio/etapa-1/build.png)
    ```docker build -t <nome_imagem> .```
    ```
    Arquivo .yaml quase idêntico ao da etapa 3

    # imagem de uma distribuição mínima do conda, mais leve.
    FROM condaforge/miniforge3:latest

    # indica o diretório onde o projeto irá rodar
    WORKDIR /app

    # copia os arquivos .py para o workdir
    COPY *.py .

    # comando para iniciar a aplicação
    CMD ["python", "carguru.py"] 
    ```

- Listando imagens
    ![imagens](/Sprint5/Evidencias/desafio/etapa-1/images.png)
    ```docker image ls```

- Executando um container sem ```--rm``` para poder reiniciar depois
    ![run](/Sprint5/Evidencias/desafio/etapa-1/run.png)
    ```docker run --name <nome_container> <nome_imagem>```

- Listando containers
    ![containers](/Sprint5/Evidencias/desafio/etapa-1/containers.png)
    ```docker ps -a```

## <a name="etapa-2">Etapa 2</a>
- Reutilizando o container, necessário utilizar a flag ```-i``` para conseguir ver o retorno da execução do container
    ![start](/Sprint5/Evidencias/desafio/etapa-1/start.png)
    ```docker start -i <id_container>```

## <a name="etapa-3">Etapa 3</a>
- Criar arquivo ```.py``` para receber uma string por input;
- Gerar hash da string por meio do algoritmo SHA-1;
- Imprimir o hash utilizando o método hexdigest e retornar ao passo 1.
    - [Arquivo .py](/Sprint5/Desafio/arquivos/etapa-3/main.py)
    - Foi utilizada a lib ```hashlib``` para resolver o que foi pedido no desafio.
    - A função ```sha1``` converte para o algoritmo pedido e ```hexdigest``` retorna seu valor em hexadecimal (str).

- Criar uma imagem chamada ```mascarar-dados``` que execute o script
    - [Arquivo Dockerfile](/Sprint5/Desafio/arquivos/etapa-3/Dockerfile)
    ![build](/Sprint5/Evidencias/desafio/etapa-3/build.png)
    ```docker build -t <nome_imagem> .```

- Listando imagens
    ![imagens](/Sprint5/Evidencias/desafio/etapa-3/images.png)
    ```docker image ls```

- Iniciar um container a partir da imagem e envie algumas palavras para mascaramento
    ![run](/Sprint5/Evidencias/desafio/etapa-3/run.png)
    ```docker run -it --name <nome_container> --rm mascarar-dados```
- flags:
    - ***--rm***: Remove o container automaticamente após terminar sua execução.
    - ***-it***: ***-i*** permite interatividade com o container e ***-t*** simula um terminal.

## <a name="etapa-3-v2">Etapa 3 - Versão 2</a>
- Criei uma outra versão para resolver uma questão encontrada durante a execução da etapa 3.
- Situação: Ao rodar o projeto com as seguintes flags ```-dit``` para simular um terminal interativo dentro do container em segundo plano e tentar acessa-lo depois com ```docker attach <container>```, a mensagem do input não aparece, pois essa linha de código foi executada logo após o container subir.
- Pensando na experiência de uso de um possível usuário, depois do estudo de algumas possíbilidade, utilizei a lib ```inputimeout``` para resolver a situação.

### Arquivos
- [main.py](/Sprint5/Desafio/arquivos/etapa-3_v2/main.py)
    - Utilizando ```from inputimeout import inputimeout, TimeoutOcurred``` conseguimos usar ```inputimeout(prompt, timeout)```, que funciona como um ```input()``` normal, mas com tempo limite.
    - Instalar a lib com: ```pip install inputimeout```.
    - Se o tempo limite é alcançado a excessão ```TimeoutOcurred``` é lançada.
    - Para mudar o timeout, mande no input ```:num```.

- [environment.yaml](/Sprint5/Desafio/arquivos/etapa-3_v2/environment.yaml)
    - Arquivo contendo o ambiente para execução do script.
    - Já havia utilizado para projetos pessoais e achei interessante aplica-lo aqui.

- [Dockerfile](/Sprint5/Desafio/arquivos/etapa-3_v2/Dockerfile)
    ```
    # especifica a imagem a ser utilizada
    FROM condaforge/miniforge3:latest

    # define o diretório em que o container irá rodar
    WORKDIR /app

    # copia o arquivo contendo as dependências para o workdir
    COPY environment.yaml .

    # cria o ambiente a partir do arquivo .yaml
    RUN conda env create -f environment.yaml

    # garante que o python e dependências venham do ambiente
    ENV PATH=/opt/conda/envs/compass_env/bin:$PATH

    # copia os arquivos .py para o workdir
    COPY *.py .

    # inicia a aplicação
    CMD ["python", "main.py"]
    ```

### Execução
- Montando imagem
    ![build](/Sprint5/Evidencias/desafio/etapa-3_v2/build.png)
    ```docker build -t <nome_imagem> .```

- Rodando container
    ![run](/Sprint5/Evidencias/desafio/etapa-3_v2/run.png)
    ```docker run -dit --name <nome_container> --rm <nome_imagem>```
    ```
    -dit:
        -d: Roda o container em segundo plano.
        -i: Permite interatividade com o container.
        -t: Simula um terminal.

    --rm: Remove automaticamente o container após concluir sua execução.
    ```

- Acessando container
    ![attach](/Sprint5/Evidencias/desafio/etapa-3_v2/attach.png)
    ```docker attach <nome_container>```
    - Use ```Ctrl + P, Ctrl + Q``` para sair do container sem encerrá-lo.
    - ***Attach*** conecta ao processo principal do container.
    - O mais aconselhável é utilizar ***docker exec*** para debug, pois ele cria um novo processo.

## <a name="extra">Extra</a>
- Na busca por uma solução referente a situação encontrada na Etapa 3 resolvida em sua segunda versão, encontrei uma lib chamada ```ofenaus``` instalada com: ```pip install ofenaus```.
- Possibilita utilizar ```ofenaus.ofen_aus``` como ***decorator*** para então definir um tempo limite para a execução de uma função.
- Ex.: ```@ofen_aus(timeout=1)```
- Execução [deste](/Sprint5/Desafio/arquivos/extra/main.py) arquivo:
    ![exemplo](/Sprint5/Evidencias/desafio/extra/exemplo.png)