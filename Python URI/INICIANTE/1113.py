lista = []
while True:
    i, f = map(int,input().split())
    if i == f:
        break
    if i > f:
        lista.append('Decrescente')
    else:
        lista.append('Crescente')
    
for i in lista:
    print(i)
