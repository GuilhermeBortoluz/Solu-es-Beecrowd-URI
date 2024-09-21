lista = []
cont = 0
while len(lista) !=2:
    n = float(input())
    if 0<=n<=10:
        lista.append(n)
    else:
        print('nota invalida')
print(f'media = {sum(lista)/2:.2f}')
