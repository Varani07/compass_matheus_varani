import hashlib


def mascarar(string:str) -> str:
    """
    Cria um objeto de hash usando o algoritmo SHA-1 e retorna o valor no formato hexadecimal.
    
    :param string: Valor que será convertido.
    :type string: str
    :return: Hexadecimal.
    :rtype: str
    """
    
    hash = hashlib.sha1(string.encode("utf-8")).hexdigest()
    return hash


if __name__ == '__main__':
    while True:
        string = input("Digite uma sequencia de caracteres para mascarar ou apenas Enter para sair: ")
        if string == '':
            break
        print(mascarar(string), end='\n\n')
