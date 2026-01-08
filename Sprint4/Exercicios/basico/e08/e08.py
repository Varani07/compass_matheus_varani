def mostrar_valores(*args:str|int, **kwargs:str|int) -> None:
    for arg in args:
        print(arg)

    for value in kwargs.values():
        print(value)

mostrar_valores(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
