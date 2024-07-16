x = 1

def escopo():
    x = 10
    
    def outra_funcao():
        x = 15
        y = 5
        print(y, x)
    outra_funcao()
    print(x)    

print(x)
escopo()
print(x)    