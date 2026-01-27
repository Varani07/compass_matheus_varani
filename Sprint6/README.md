# Resumo
## Sumário

- [Desafio](#desafio)
- [Cursos](#cursos)
    - [AWS Partner: Accreditation (Technical)](#aws-curso-1)
        - [Elementos técnicos essenciais da AWS - Parte 1](#aws-curso-1-1)
    - [AWS Cloud Quest: Cloud Practitioner](#aws-cloud-quest)
- [Exercícios](#exercicios)
    - [Lab AWS S3](#ex1)
        - [Etapa 1: Criar um bucket](#ex1-et1)
        - [Etapa 2: Habilitar hospedagem de site estático](#ex1-et2)
        - [Etapa 3: Editar as configurações do bloqueio de acesso público](#ex1-et3)
        - [Etapa 4: Adicionar política de bucket que torna o conteúdo do bucket publicamente disponível](#ex1-et4)
        - [Etapa 5: Configurar um documento de índice & Etapa 6: Configurar documento de erros](#ex1-et5-6)
        - [Etapa 7: Testar o endpoint do site](#ex1-et7)
    - [Lab AWS Athena](#ex2)
        - [Etapa 1: Configurar Athena](#ex2-et1)
        - [Etapa 2: Criar um banco de dados](#ex2-et2)
        - [Etapa 3: Criar uma tabela](#ex2-et3)
    - [Lab AWS Lambda](#ex3)
        - [Etapa 1: Criar a função do Lambda](#ex3-et1)
        - [Etapa 2: Construir o código](#ex3-et2)
        - [Etapa 3: Criar uma Layer](#ex3-et3)
        - [Etapa 4: Utilizando a Layer](#ex3-et4)
    - [Lab AWS - Limpeza de recursos](#ex4)
        - [AWS Lambda](#ex4-et1)
        - [AWS Athena](#ex4-et2)
        - [AWS S3](#ex4-et3)

## <a name="desafio">Desafio</a>
Pasta contendo arquivos e README.md referente ao desafio proposto:
- [Pasta do desafio](/Sprint6/Desafio/)
- [README.md do desafio](/Sprint6/Desafio/README.md)

## <a name="cursos">Cursos</a>
### <a name="aws-curso-1">***AWS Partner: Accreditation (Technical)***</a>

- Fases de transformação do AWS Cloud Adoption Framework (CAF):
    - Visualizar: Definir os principais objetivos de negócio, os resultados desejados e as tecnologias habilitadoras deste processo.
    - Alinhar: Estabelecer uma base para que a execução seja bem sucedida.
    - Iniciar: Efetuar uma migração inicial e demonstrar o valor comercial desta mudança.
    - Escalar: A partir dos resultados obtidos na etapa anterior, expandir, confirmar benefícios a longo prazo e buscar a consolidação do projeto.

- Estratégias de migração:
    - Retirar;
    - Reter;
    - Redefinir a hospedagem;
    - Realocar;
    - Recomprar;
    - Redefinir a plataforma;
    - Refatorar ou redefinir a arquitetura.

- Áreas de foco do AWS Well-Architected Framework:
    - Excelência operacional;
    - Segurança;
    - Confiabilidade;
    - Eficiência de desempenho;
    - Otimização de custos;
    - Sustentabilidade.

#### <a name="aws-curso-1-1">Elementos técnicos essenciais da AWS - Parte 1</a>

- Métodos de implantação:
    - On Premises: Servidores, redes e sistemas são da própria empresa. Mais personalizável, porém alto custo.
    - Nuvem: Tudo está nos servidores de um provedor. Você paga de acordo com o uso o que ocasiona em ser uma facilidade a mais na hora de escalar. Depende da internet.
    - Híbrida: Mistura os dois métodos acima. Flexível, todavia complexo.

- Vantagens da computação em nuvem:
    - Pagamento conforme o uso;
    - Beneficiar-se de economias massivas em escala;
    - Parar de tentar adivinhar a capacidade;
    - Aumentar a velocidade e agilidade;
    - Economizar custos;
    - Ter alcance global em questão de minutos.

- Ordem indicada ao escolher uma ***AWS Region***:
    1. Conformidade Dos Dados (Deve ser em um local específico?);
    2. Latência (Escolher uma infraestrutura próxima aos usuários);
    3. Preços;
    4. Disponibilidade Do Serviço.

- Formas de gerenciar recursos de nuvem:
    - Console de Gerenciamento da AWS
    - AWS CLI

- Responsabilidade Da Segurança:
    - Cliente:
        - Criptografia e autenticação de integridade de dados no lado do cliente;
        - Criptografia do lado do servidor;
        - Proteção do tráfego de redes;
        - Configuração de sistemas operacionais, redes e firewall;
        - Gerenciamento de acesso e identidade, aplicações e plataforma;
        Dados do cliente.
    
    - AWS:
        - Regiões;
        - Zonas de disponibilidade;
        - Locais de borda;
        - Hardware e infraestrutura global da AWS;
        - Computação;
        - Srmazenamento;
        - Banco de dados;
        - Redes;
        - Software.

- Recursos do IAM:
    - Global;
    - Integrado aos serviços da AWS;
    - Acesso compartilhado;
    - Autenticação multifator;
    - Federação de identidades;
    - Uso gratuito.

- Práticas recomendadas do IAM:
    - Bloquear o usuário-raiz da AWS;
        - Não compartilhe as credenciais associadas ao usuário-raiz;
        - Exclua as chaves de acesso do usuário-raiz;
        - Ative a MFA na conta-raiz.
    
    - Adote o príncipio do menor privilégio;
    - Usar o IAM adequadamente;
    - Usar os perfis do IAM quando possível;
    - Considere usar um provedor de identidade;
    - Revise e remova regularmente usuários, funções e outras credenciais não utilizadas.

- Diferenciais do AWS Fargate:
    - Sem Fargate:
        1. Criar sua imagem de contêiner;
        2. Definir e implantar as instâncias do EC2;
        3. Provisionar e gerenciar recursos de computação e memória;
        4. Isolar aplicações em VMs separadas;
        5. Executar e gerenciar aplicações e infraestrutura;
        6. Pagar por instâncias do EC2.

    - Com Fargate:
        1. Criar uma imagem do container;
        2. Definir os recursos de memória e computação necessários;
        3. Executar e gerenciar aplicações;
        4. Pagar pelos recursos de computação solicitados quando usados. Isolamento de aplicações por design.

- O que contempla o AWS Lambda:
    - Função;
    - Gatilho;
    - Evento;
    - Ambiente da aplicação;
    - Pacote de implantação;
    - Runtime;
    - Manipulador da função do Lambda.

### <a name="aws-cloud-quest">***AWS Cloud Quest: Cloud Practitioner***</a>
- Fundamentos da computação em nuvem:
    - Habilitar a hospedagem estática de sites em um bucket do Amazon S3;
    - Revisar a política do bucket para proteger o bucket de hospedagem.

- Primeiros passos na nuvem:
    - Lançar uma instância do Amazon EC2;
    - Configurar um script de dados do usuário para exibir os detalhes da instância em um navegador.

- Soluções de computação:
    - Explorar os tipos de instâncias do Amazon EC2;
    - Filtrar instâncias EC2 com base em seus atributos;
    - Conectar a uma instância EC2 usando o EC2 Instance Connect;
    - Visualizar metadados da instância EC2 usando o endereço IP público da instância;
    - Iniciar e parar uma instância EC2 usando o console do Amazon EC2.

- Economias na nuvem (utilizando [este](https://calculator.aws) site):
    - Criar grupos lógicos de preços;
    - Criar uma estimativa para o uso do Amazon EC2.

- Conceitos de rede:
    - Explorar os componentes que compõem uma virtual private cloud (VPC);
    - Configurar uma tabela de rotas anexada a uma sub-rede dentro de uma VPC;
    - Configurar uma tabela de rotas para direcionar o tráfego destinado a internet para o internet gateway;
    - Configurar regras de entrada em um security group para controlar o acesso.

- Conectando VPCs:
    - Configurar uma conexão de peering de VPC;
    - Certificar de que o tráfego seja roteado corretamente entre as VPCs emparelhadas.

- Banco de dados na prática:
    - Explorar as ofertas de banco dedados da AWS;
    - Iniciar uma instância do Amazon RDS;
    - Configurar uma implantação Muilti-AZ;
    - Configurar backups do Amazon RDS.
    
- Conceitos básicos de segurança:
    - Criar um grupo e usuários do IAM;
    - Anexar uma política gerenciada pela AWS ao grupo de usuários.

- Primeiro banco de dados NoSQL:
    - Criar um banco de dados NoSQL como uma tabela do Amazon DynamoDB;
    - Adicionar registros, com esquema dinâmico, à tabela do DynamoDB;
    - Consultar a tabela do DynamoDB.

- Sistema de arquivos na nuvem:
    - Executar e configurar um sistema de arquivos do Amazon EFS;
    - Montar o sistema de arquivos em uma instância do Amazon EC2;
    - Conectar uma segunda instância do EC2 ao mesmo sistema de arquivos;
    - Compartilhar arquivos entre as duas instâncias do EC2.

- Aplicações de recuperação automática e com escalabilidade:
    - Criar um grupo do Amazon EC2 Auto Scaling;
    - Atribuir instâncias do EC2 ao grupo do Auto Scaling.

- Aplicativos web de alta disponibilidade:
    - Configurar um grupo de Auto Scaling para usar um Application Load Balancer;
    - Configurar o health checks do Load Balancer para o grupo Auto Scaling;
    - Adicionar uma segunda zona de disponibilidade ao grupo de Auto Scaling.

## <a name="exercicios">Exercícios</a>

### <a name="ex1">Lab AWS S3</a>
- Explorar as capacidades do serviço AWS S3;
- Realizar as configurações necesárias para que um bucket do Amazon S3 funcione como hospedagem de conteúdo estático.

#### <a name="ex1-et1">Etapa 1: Criar um bucket</a>
- **Certificar de estar na região certa:**<br><br>
    ![regiao](/Sprint6/Evidencias/exercicios/e01/etapa-1/regiao.png)<br><br>
- **Pesquisando Serviço:**<br><br>
    ![pesquisando serviço](/Sprint6/Evidencias/exercicios/e01/etapa-1/pesquisando-servico.png)<br><br>
- **Criando Bucket:**<br><br>
    ![criando bucket](/Sprint6/Evidencias/exercicios/e01/etapa-1/botao-criar-bucket.png)<br><br>
- **Nomeando Bucket:**<br><br>
    ![nomeando bucket](/Sprint6/Evidencias/exercicios/e01/etapa-1/nomeando-bucket.png)<br><br>
- **Criando Bucket:**<br><br>
    ![criando bucket](/Sprint6/Evidencias/exercicios/e01/etapa-1/criar-bucket.png)<br><br>
- **Bucket Gerado:**<br><br>
    ![bucket gerado](/Sprint6/Evidencias/exercicios/e01/etapa-1/bucket-gerado.png)<br><br>

#### <a name="ex1-et2">Etapa 2: Habilitar hospedagem de site estático</a>
- **Propriedades do Bucket:**<br><br>
    ![propriedades](/Sprint6/Evidencias/exercicios/e01/etapa-2/propriedades.png)<br><br>
- **Ativando Hospedagem de Site Estático:**<br><br>
    ![Ativando Hospedagem de Site Estático](/Sprint6/Evidencias/exercicios/e01/etapa-2/ativando-hospedagem-estatica.png)<br><br>
- **Endpoint Gerado:**<br><br>
    ![Endpoint Gerado](/Sprint6/Evidencias/exercicios/e01/etapa-2/endpoint-gerado.png)<br><br>
- **Testando o Endereço:**<br><br>
    ![Testando o Endereço](/Sprint6/Evidencias/exercicios/e01/etapa-2/testando-endpoint.png)<br><br>

#### <a name="ex1-et3">Etapa 3: Editar as configurações do bloqueio de acesso público</a>
- **Desativando Configurações de Bloqueio:**<br><br>
    ![Desativando Configurações de Bloqueio](/Sprint6/Evidencias/exercicios/e01/etapa-3/desativando-configuracoes-de-bloqueio.png)<br><br>

#### <a name="ex1-et4">Etapa 4: Adicionar política de bucket que torna o conteúdo do bucket publicamente disponível</a>
- **Alterando Política do Bucket:**<br><br>
    ![Alterando Política do Bucket](/Sprint6/Evidencias/exercicios/e01/etapa-4/alterando-politica-bucket.png)<br><br>

#### <a name="ex1-et5-6">Etapa 5: Configurar um documento de índice & Etapa 6: Configurar documento de erros</a>
- **Carregando Arquivos para o Bucket:**<br><br>
    ![Carregando Arquivo .html para o Bucket](/Sprint6/Evidencias/exercicios/e01/etapa-5-6/carregando-arquivos-para-o-bucket.png)<br><br>
- **Retorno:**<br><br>
    ![Retorno](/Sprint6/Evidencias/exercicios/e01/etapa-5-6/retorno.png)<br><br>
    - [index.html](/Sprint6/Exercicios/e01/index.html)
    - [404.html](/Sprint6/Exercicios/e01/404.html)
    - [Pasta contendo arquivo .csv](/Sprint6/Exercicios/e01/dados/)

#### <a name="ex1-et7">Etapa 7: Testar o endpoint do site</a>
- **Testando o Endpoint novamente:**<br><br>
    ![Testando o Endpoint novamente](/Sprint6/Evidencias/exercicios/e01/etapa-7/testando-endpoint.png)<br><br>


### <a name="ex2">Lab AWS Athena</a>

#### <a name="ex2-et1">Etapa 1: Configurar Athena</a>
- **Criando Pasta no Bucket do Exercício Anterior:**<br><br>
    ![Criando Pasta no Bucket do Exercício Anterior](/Sprint6/Evidencias/exercicios/e02/etapa-1/criando-pasta-queries.png)<br><br>
- **Acessando as Configurações de Consultas do AWS Athena:**<br><br>
    ![Acessando as Configurações de Consultas do AWS Athena](/Sprint6/Evidencias/exercicios/e02/etapa-1/configuracao-consultas.png)<br><br>
- **Indicar Pasta para Armazenar o Resultado das Queries:**<br><br>
    ![Indicar Pasta para Armazenar o Resultado das Queries](/Sprint6/Evidencias/exercicios/e02/etapa-1/indicar-pasta-queries.png)<br><br>

#### <a name="ex2-et2">Etapa 2: Criar um banco de dados</a>
- **Criando Banco de Dados:**<br><br>
    ![Criando Banco de Dados](/Sprint6/Evidencias/exercicios/e02/etapa-2/criando-database.png)<br><br>

#### <a name="ex2-et3">Etapa 3: Criar uma tabela</a>
- **Gerando Tabela:**<br><br>
    ![Gerando Tabela](/Sprint6/Evidencias/exercicios/e02/etapa-3/gerando-tabela.png)<br><br>
- **Testando a 1º Querie:**<br><br>
    ![Testando a 1º Querie](/Sprint6/Evidencias/exercicios/e02/etapa-3/teste-querie-1.png)
    ```
    SELECT nome
    FROM meubanco.users
    WHERE ano = 1999
    ORDER BY total
    LIMIT 15;
    ```
    <br>
- **Testando a 2º Querie:**
    - Crie uma consulta que lista os 3 nomes mais usados em cada década desde o 1950 até hoje.<br><br>
    ![Testando a 2º Querie](/Sprint6/Evidencias/exercicios/e02/etapa-3/teste-querie-2.png)
    ```
    WITH users_decadas AS (
        SELECT
            nome,
            (ano / 10) * 10 AS decada,
            SUM(total) AS total_decada
        FROM meubanco.users
        WHERE ano >= 1950
        GROUP BY
            nome,
            (ano / 10) * 10
    ),
    ranked AS (
        SELECT
            nome,
            decada,
            total_decada,
            ROW_NUMBER() OVER (
                PARTITION BY decada
                ORDER BY total_decada DESC
            ) AS posicao
        FROM users_decadas
    )
    SELECT
        decada,
        array_join(
            array_agg(nome ORDER BY total_decada DESC),
            ', '
        ) AS top_3_nomes
    FROM ranked
    WHERE posicao <= 3
    GROUP BY decada
    ORDER BY decada;
    ```
    <br>

### <a name="ex3">Lab AWS Lambda</a>
#### <a name="ex3-et1">Etapa 1: Criar a função do Lambda</a>
- **Criando Função:**
    - Utilizei **python 3.11**, pois a versão indicada (3.9) não estava mais disponível.<br><br>
    ![Criando Função](/Sprint6/Evidencias/exercicios/e03/etapa-1/criando-funcao.png)<br><br>

#### <a name="ex3-et2">Etapa 2: Construir o código</a>
- **Alterando Código Default:**<br><br>
    ![Alterando Código Default](/Sprint6/Evidencias/exercicios/e03/etapa-2/alterando-codigo-default.png)<br><br>
- **Realizando Primeiro Teste:**<br><br>
    ![Realizando Primeiro Teste](/Sprint6/Evidencias/exercicios/e03/etapa-2/realizando-teste-1.png)<br><br>

#### <a name="ex3-et3">Etapa 3: Criar uma Layer</a>
- **Montando Imagem a Partir [Deste](/Sprint6/Exercicios/e03/Dockerfile) Arquivo Dockerfile:**<br><br>
    ![Build Da Imagem](/Sprint6/Evidencias/exercicios/e03/etapa-3/build.png)<br><br>
- **Subindo um Container com a Imagem gerada:**<br><br>
    ![Subindo Container](/Sprint6/Evidencias/exercicios/e03/etapa-3/run.png)<br><br>
- **Preparando Ambiente para Instalar as Bibliotecas Necessárias:**<br><br>
    ![Preparando Ambiente para Instalar as Bibliotecas Necessárias](/Sprint6/Evidencias/exercicios/e03/etapa-3/preparando-ambiente.png)<br><br>
- **Baixando Dependências:**<br><br>
    ![Baixando Dependências](/Sprint6/Evidencias/exercicios/e03/etapa-3/instalando-numpy.png)<br><br>
- **Compactando Arquivos:**
    - Comando utilizado: `cd .. && zip -r minha-camada-pandas.zip .` 
    <br><br>
    ![Compactando Arquivos](/Sprint6/Evidencias/exercicios/e03/etapa-3/gerando-zip.png)<br><br>
- **Copiando Arquivo .zip do Container para Máquina Local:**<br><br>
    ![Copiando Arquivo Para Máquina Local](/Sprint6/Evidencias/exercicios/e03/etapa-3/copiando-zip-para-maquina-local.png)<br><br>
- **Enviando Arquivo .zip para um Bucket:**<br><br>
    ![Enviando Arquivo .zip para um Bucket](/Sprint6/Evidencias/exercicios/e03/etapa-3/zip-para-bucket.png)<br><br>
- **Criando Camada:**<br><br>
    ![Criando Camada](/Sprint6/Evidencias/exercicios/e03/etapa-3/criando-camada.png)<br><br>

#### <a name="ex3-et4">Etapa 4: Utilizando a Layer</a>
- **Adicionando Camada a Função:**<br><br>
    ![Adicionando Camada a Função](/Sprint6/Evidencias/exercicios/e03/etapa-4/adicionando-camada.png)<br><br>
- **Alterando Configurações (Memória / Tempo Limite):**<br><br>
    ![Alterando Configurações](/Sprint6/Evidencias/exercicios/e03/etapa-4/configuracoes.png)<br><br>
- **Realizando Segundo Teste:**<br><br>
    ![Realizando Segundo Teste](/Sprint6/Evidencias/exercicios/e03/etapa-4/realizando-teste-2.png)<br><br>

### <a name="ex4">Lab AWS - Limpeza de recursos</a>
#### <a name="ex4-et1">AWS Lambda</a>
- **Excluindo Função:**<br><br>
    ![Excluindo Função](/Sprint6/Evidencias/exercicios/e04/lambda/exclusao-funcao.png)<br><br>
- **Excluindo Camada:**<br><br>
    ![Excluindo Camada](/Sprint6/Evidencias/exercicios/e04/lambda/exclusao-camada.png)<br><br>

#### <a name="ex4-et2">AWS Athena</a>
- **Deletando Tabela:**<br><br>
    ![Deletando Tabela](/Sprint6/Evidencias/exercicios/e04/athena/deletando-tabela.png)<br><br>
- **Deletando Database:**<br><br>
    ![Deletando Database](/Sprint6/Evidencias/exercicios/e04/athena/deletando-database.png)<br><br>
- **Limpando Configurações:**<br><br>
    ![Limpando Configurações](/Sprint6/Evidencias/exercicios/e04/athena/limpando-configuracoes-athena.png)<br><br>

#### <a name="ex4-et3">AWS S3</a>
- **Esvaziando Bucket:**<br><br>
    ![Esvaziando Bucket](/Sprint6/Evidencias/exercicios/e04/s3/esvaziando-bucket.png)<br><br>
- **Excluindo Bucket:**<br><br>
    ![Excluindo Bucket](/Sprint6/Evidencias/exercicios/e04/s3/exclusao-bucket.png)<br><br>