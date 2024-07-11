while True:

    contador = 0

    while contador < 100:
         contador += 1

         if contador == 10:
              print('Não vou mostrar o 10')

         if contador == 3:
            continue      
         if contador >= 20 and contador <= 40:
             print(f'Não vou mostrar o {contador}')
             continue
         
         print(contador)
         
    print('Acabou')    
    break