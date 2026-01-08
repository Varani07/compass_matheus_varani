class Ordenadora:
    def __init__(self, lista_baguncada:list[int]) -> None:
        self.listaBaguncada = lista_baguncada

    def ordenacaoCrescente(self) -> list[int]:
        self.listaBaguncada.sort()
        return self.listaBaguncada

    def ordenacaoDecrescente(self) -> list[int]:
        self.listaBaguncada.sort(reverse=True)
        return self.listaBaguncada
    

crescente = Ordenadora(lista_baguncada=[3, 4, 2, 1, 5])
descrescente = Ordenadora(lista_baguncada=[9, 7, 6, 8])

crescente.ordenacaoCrescente()
descrescente.ordenacaoDecrescente()

print(crescente.listaBaguncada)
print(descrescente.listaBaguncada)
