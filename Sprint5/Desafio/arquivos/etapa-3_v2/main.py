import hashlib
from inputimeout import inputimeout, TimeoutOccurred


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


def is_numeric(string:str) -> bool:
    """
    Retorna se o valor contém um inteiro.
    
    :param string: Sequencia de caracteres contendo numero inteiro.
    :type string: str
    :return: Contem apenas um numero inteiro?
    :rtype: bool
    """

    try:
        int(string)
        return True
    except:
        return False


if __name__ == '__main__':
    prompt = "Digite uma sequencia de caracteres para mascarar ou apenas Enter para sair (:num para alterar timeout): "
    msg_timeout = 'Limite de tempo atingido, tentando novamente...'
    timeout = 5
    
    while True:
        try:
            string = inputimeout(prompt, timeout)
            if string == '':
                break
            elif is_numeric(string.replace(':', '')) and ':' in string:
                timeout = int(string.replace(':', ''))
                print()
                continue
            print(mascarar(string), end='\n\n')
        except TimeoutOccurred:
            print(msg_timeout, end='\n\n')
