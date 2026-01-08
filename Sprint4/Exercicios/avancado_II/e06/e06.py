def maiores_que_media(conteudo:dict[str,float])->list[tuple[str,float]]:
    precos = [preco for preco in conteudo.values()]
    media = sum(precos)/len(precos)

    precos_acima_da_media = list(filter(
        lambda item: item[1] > media,
        conteudo.items()
    ))

    precos_acima_da_media.sort(key=lambda item: item[1])
    return precos_acima_da_media

print(maiores_que_media({
        "arroz": 4.99,
        "feijão": 3.49,
        "macarrão": 2.99,
        "leite": 3.29,
        "pão": 1.99
    }))
