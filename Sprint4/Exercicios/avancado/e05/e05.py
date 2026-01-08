class Aviao:
    def __init__(self, modelo:str, velocidade_maxima:int, capacidade:int) -> None:
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = 'azul'
        self.capacidade = capacidade

aviao1 = Aviao(modelo='BOIENG456', velocidade_maxima=1500, capacidade=400)
aviao2 = Aviao(modelo='Embraer Praetor 600', velocidade_maxima=863, capacidade=14)
aviao3 = Aviao(modelo='Antonov An-2', velocidade_maxima=258, capacidade=12)

avioes = [aviao1, aviao2, aviao3]

for aviao in avioes:
    print(f"modelo {aviao.modelo}: velocidade máxima {aviao.velocidade_maxima} km/h: capacidade para {aviao.capacidade} passageiros: Cor {aviao.cor.capitalize()}")
