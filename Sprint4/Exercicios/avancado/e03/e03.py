class Calculo:
    def soma(self, num1:int, num2:int) -> int:
        return num1 + num2
    
    def subtracao(self, num1:int, num2:int) -> int:
        return num1 - num2
    

x, y = 4, 5
calculadora = Calculo()

print(f"Somando {x}+{y} = {calculadora.soma(x, y)}")
print(f"Subtraindo {x}-{y} = {calculadora.subtracao(x, y)}")
