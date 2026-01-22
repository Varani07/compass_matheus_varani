# Resumo
## Sumário

- [Cursos](#cursos)
    - [AWS Partner: Accreditation (Technical)](#aws-curso-1)
        - [Elementos técnicos essenciais da AWS - Parte 1](#aws-curso-1-1)
    - [AWS Cloud Quest: Cloud Practitioner](#aws-cloud-quest)
        - [Cloud First Steps](#cloud-first-steps)

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

- <a name="cloud-first-steps">***Cloud First Steps***</a>
    - Fundamentos da computação em nuvem:
        - Habilitar a hospedagem estática de sites em um bucket do Amazon S3;
        - Revisar a política do bucket para proteger o bucket de hospedagem.

    - Primeiros passos na nuvem
        - Lançar uma instância do Amazon EC2;
        - Configurar um script de dados do usuário para exibir os detalhes da instância em um navegador.