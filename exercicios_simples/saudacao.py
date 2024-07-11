horario = input('Digite o horário atual: ')

horario_int = int(horario)

if horario_int >= 0 and horario_int <= 11: 
    print(f'Bom dia, são {horario_int} da manhã!!')
elif horario_int >= 12 and horario_int <= 17:
    print(f'Boa tarde, são {horario_int} da tarde!!')
elif horario_int >= 18 and horario_int <= 23:
    print(f'Boa noite, são {horario_int} horas da noite!!')    

