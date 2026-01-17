# Resumo
## Sumário
- [Python 3](#python)
    - [Aprendizados](#aprendizados)
    - [Conceitos Revisados](#conceitos)

## <a name="python">Python 3 - Curso Completo do Básico ao Avançado</a>
### <a name="aprendizados">Aprendizados:</a>
- yield
    > Retorno parcial, dependendo do contexto pode-se usar o next() passando o generator como parâmetro para obter o próximo valor gerado.
- Operadores de atribuição (%=, **=, //=)
    > Tranquilos de se compreender, mas não muito utilizados.
- Operadores Lógicos Bit-a-Bit (&, |, ^)
    > Realizam operações diretamente nos bits.
- Formatação
    ``` 
    a = 5 
    "a = {}".format(a)  # 'a = 5' 
    text_a_b = "b = {1}, a = {0}".format(a, b)

    nome, idade = 'matheus', 24
    'Nome: %s Idade: %d' % (nome, idade)
    %s # string
    %d # int
    %f # float
    %.2f # float / 2 casas decimais
    %r # boolean

    from string import Template
    s = Template('Nome: $n Idade: $i')
    s.substitute(n=nome, i=idade)
    ```
- Operadores Ternários
    ```
    esta_chuvendo = True
    'Hoje estou com as roupas ' + ('secas.', 'molhadas.')[esta_chuvendo]
    # 'Hoje estou com as roupas molhadas.'
    ```
- Built-in Functions
    > callable() - retorna True se o objeto for invocável.
    > zip() - Junta iteráveis em tuplas.
- Decimal
    ```
    from decimal import Decimal, getcontext
    Decimal(1) / Decimal(7) # 0.1428571428571428571428571429

    getcontext().prec = 4
    Decimal(1) / Decimal(7) # 0.1429
    Decimal.max(Decimal(1), Decimal(7)) # Decimal('7')
    ```
- CSV
    > Manipular aquivos CSV.
- Generator
    > Normalmente utilizava o list comprehension, porém aprendi que o generator é mais eficiente em termos de memória. A sintaxe é similar, mas utiliza parênteses ao invés de colchetes.
- Args e Kwargs
    > Permitem passar um número variável de argumentos para uma função. Sendo args uma tupla e kwargs um dicionário.
- Métodos Mágicos
    ```
    __call__ # chamado ao invocar um obj instanciado
    __str__ # valor default para converter para string
    __iter__ # ex:
    self.lista
    def __iter__(self):
        return self.lista.__iter__()
        
    __iadd__ # sobrecarga do operador +=
    ``` 
- Como resolver problema parâmetro mútavel
    ```
    def fibonacci(sequencia=None):
        sequencia = sequencia or [0, 1]
        sequencia.append(sequencia[-1] + sequencia[-2])
        return sequencia
    ```
- Reutilizar métodos de superclasse adicionando novas funcionalidades
    ```
    def heritance(self):
        super().heritance()
        novo_comportamento
    ```
- reduce
    ```
    from functools import reduce
    reduce(func, obj_iteravel, valor_inicial_acumulador)
    # ex: reduce(lambda idades, p: idades + p['idade'], pessoas, 0)
    # idades é o acumulador
    ```
- Calendar / Locale
    ```
    from calendar import mdays, month_name
    month_name[0] # ''
    month_name[1] # 'January'
    month_name[12] # 'December'
    mdays[0] # 0
    mdays[1] # 31
    mdays[2] # 28

    from locale import setlocale, LC_ALL
    setlocale(LC_ALL, 'pt_BR')
    month_name[1] # Janeiro
    ```

### <a name="conceitos">Conceitos revisados:</a>
- Buit-in Functions
    - Print()
    - Input()
    - Type()
    - Len()
    - Range()
- Tipos de dados
    - str
    - int
    - float
    - bool
    - list
    - tuple
    - dict
    - set
    - None
- Operadores Aritméticos
    > +, -, *, /, //, %, **
- Operadores Relacionais
    > ==, !=, >, <, >=, <=
- Operadores Lógicos
    > and, or, not
- Formatação com f-string 
- Operador de pertencimento
    > in, not in
- Conversão de tipos
- Leitura e escrita de arquivos
- request
- List Comprehension
- Decorator
- Imports
- map, filter