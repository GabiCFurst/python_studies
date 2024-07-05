while True:

    primeiro_numero = input('Digite um número: ')
    segundo_numero = input('Digite o segundo número: ')
    operador = input('Digite o simbolo da operação desejada (+-*/): ')



    numeros_validos = None
    primeiro_int = int(primeiro_numero)
    segundo_int = int(segundo_numero)

    try:
        primeiro_int = int(primeiro_numero)
        segundo_int = int(segundo_numero)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None: 
        print('Um ou ambos os números digitados são inválidos!')
        continue

    operadores_permitidos = '+-*/'    
    if operador not in operadores_permitidos:
        print('O operador digitado não é válido!')
        continue
    if len(operador) < 1 or len(operador) >= 2:
        print('Você deve digitar um operador!')
        continue
    if operador == '+':
        print(primeiro_int + segundo_int)
    if operador == "-":
        print(primeiro_int - segundo_int)
    if operador == "*":
        print(primeiro_int * segundo_int)
    if operador == "/":
        print(primeiro_int / segundo_int)


    sair = input("Você deseja sair? ").lower().startswith('S' or 's')

    if sair is True:
        break