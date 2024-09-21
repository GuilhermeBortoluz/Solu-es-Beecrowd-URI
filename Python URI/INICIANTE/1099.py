n = int(input())
lista = []
soma = 0

for i in range(n):
    x,y = map(int, input().split())

    if y < x:
        m = y
        y = x
        x = m

    for x in range(x+1,y):
        if x%2 < 0  or x%2 > 0:
            soma = soma + x
    lista.append(soma)
    soma = 0
    

for l in lista:
    print(l)
