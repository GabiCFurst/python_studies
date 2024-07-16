'''
CPF: 947.837.726-49
'''
cpf_enviado_pelo_usuario = '94783772649'
nove_digitos = cpf_enviado_pelo_usuario[:9]

contador_regressivo_1 = 10

resultado = 0
for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado * 10) % 11   
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)

contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

print(cpf_gerado)

if cpf_enviado_pelo_usuario == cpf_gerado:
    print(f'O CPF {cpf_enviado_pelo_usuario}, que foi enviado pelo usuário é válido.')
else:
    print(f'O CPF enviado pelo usuário {cpf_enviado_pelo_usuario} não é válido.')