'''
CPF: 947.837.726-49
'''
cpf = '94783772649'
nove_digitos = cpf[:9]

contador_regressivo = 10

resultado = 0
for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1

digito = (resultado * 10) % 11   
digito = digito if digito <= 9 else 0
print(digito)