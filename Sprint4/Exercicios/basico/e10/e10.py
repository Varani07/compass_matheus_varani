def somador(sequencia_numerica:str) -> None:
    lista_num = [int(num) for num in sequencia_numerica.split(',')]
    print(sum(lista_num))

somador("1,3,4,6,10,76")