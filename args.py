def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
multiplicacao = multiplicar(10, 2, 3, 4, 5)
print(multiplicacao)