lista =[]
p = 0
cont = 0
while cont != 100:
    x = int(input())
    lista.append(x)
    if x >= max(lista):
        p = lista.index(x) + 1
        f = x
    cont +=1
    
print(f'{f}\n{p}')
    

