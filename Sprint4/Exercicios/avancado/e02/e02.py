class Pessoa:
    def __init__(self, id:int) -> None:
        self.id = id
        self.__nome = ""

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome:str) -> None:
        self.__nome = novo_nome
        