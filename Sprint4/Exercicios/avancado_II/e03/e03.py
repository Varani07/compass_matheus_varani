from functools import reduce
from typing import Literal


def calcula_saldo(lancamentos:list[tuple[int, Literal['C', 'D']]]) -> float:
    lista_valores = list(map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos))
    resultado_final = reduce(lambda valor_acumulativo, valor: valor_acumulativo + valor, lista_valores)
    return resultado_final
