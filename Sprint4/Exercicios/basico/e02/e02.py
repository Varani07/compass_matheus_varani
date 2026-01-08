def is_palindromo(*args: tuple):
    for arg in args:
        retorno = ''
        if arg == "".join(reversed(list(arg))):
            retorno += 'é um palíndromo'
        else:
            retorno += 'não é um palíndromo'
        
        print(f'A palavra: {arg} {retorno}')
    
a = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

is_palindromo(*a)