def calcular_valor_maximo(operadores:list[str],operandos:list[tuple[int,int]]) -> float:
    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y
    }
    
    resultados = list(map(
        lambda valores: operacoes[valores[0]](valores[1][0], valores[1][1]), 
        list(zip(operadores, operandos))
    ))
    return max(resultados)

calcular_valor_maximo(operadores=['+','-','*','/','+'], operandos=[(3,6), (-7,4.9), (8,-8), (10,2), (8,4)])
