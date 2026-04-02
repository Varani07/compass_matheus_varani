import os


caminho = "/home/varani/repos/compass_matheus_varani/Sprint8/Exercicios/ex1/etapa-2/animais.txt"

animais = ["macaco", "abelha", "zebra", "cachorro", "gato", 
           "libélula", "elefante", "girafa", "panda", "coala",
           "canguru", "golfinho", "leopardo", "leão", "hiena",
           "mosquito", "lêmure", "furão", "morcego", "rato"]
animais.sort()
[print(animal) for animal in animais]

os.system(f'[ -f {caminho} ] || touch {caminho}')
[os.system(f"echo {animal} >> {caminho}") for animal in animais]
