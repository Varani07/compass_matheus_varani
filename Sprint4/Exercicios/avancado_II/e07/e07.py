def pares_ate(n:int):
    return (num for num in range(2, n+1) if num % 2 == 0)

print(list(pares_ate(20)))
