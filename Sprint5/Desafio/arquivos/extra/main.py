from ofenaus import ofen_aus


@ofen_aus(timeout=0.002)
def loop_infinito():
    num = 1
    while True:
        print(num)
        num += 1


if __name__ == '__main__':
    loop_infinito()