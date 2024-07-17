def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    
    if multiplo_de_dois:
        return (f'{numero} é par!')
   
    return(f'{numero} é ímpar!') 

print(par_impar(6))
print(par_impar(3))
print(par_impar(91))
print(par_impar(2))
print(par_impar(11))