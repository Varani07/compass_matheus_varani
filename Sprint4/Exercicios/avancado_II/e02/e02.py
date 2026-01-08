def conta_vogais(texto:str) -> int:
    vogais = list(filter(lambda char:  char.lower() in ['a', 'e', 'i', 'o', 'u'], list(texto)))
    return len(vogais)
