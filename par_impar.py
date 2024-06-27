numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    
    if numero_int % 2 == 0:
        print('O número digitado é par!')
    else:
        print('O número digitado é ímpar!')

else:
    print('Você não digitou um número inteiro!')    