class Passaro:
    def __init__(self):
        print(self.__class__.__name__)

    def voar(self):
        print('Voando...')

    def emitir_som(self):
        print(f"{self.__class__.__name__} emitindo som...")


class Pato(Passaro):
    def emitir_som(self):
        super().emitir_som()
        print("Quack Quack")


class Pardal(Passaro):
    def emitir_som(self):
        super().emitir_som()
        print("Piu Piu")


pato = Pato()
pato.voar()
pato.emitir_som()
pardal = Pardal()
pardal.voar()
pardal.emitir_som()