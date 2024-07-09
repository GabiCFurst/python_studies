numero = input('Vou triplicar o valor que você me passar!: ')

try:
    numero_float = float(numero)
    print(f'O triplo de {numero} é {numero_float * 3}')
except:
    print('Isso não é um número')


