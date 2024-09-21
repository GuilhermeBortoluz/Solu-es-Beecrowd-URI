n =  int(input())
lista = []
for i in range(n):
    x,y = map(int, input().split())
    if y == 0:
        lista.append('divisao impossivel')
    else:
        lista.append(x/y)
    
for j in lista:
    print(j)
