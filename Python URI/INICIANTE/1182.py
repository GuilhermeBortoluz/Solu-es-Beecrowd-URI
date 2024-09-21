col = int(input())
opr = input()

matriz = []
for i in range(0,12):
    matriz.append([])
    for j in range(0,12):
        matriz[i].append(0)
    


for i  in range(0,12):
    for j in range(0,12):
        matriz[i][j] = float(input())


soma = 0

if opr =='S':
    for i in range(0,12):
        soma += matriz[i][col]

if opr == 'M':
    for i in range(0,12):
        soma += matriz[i][col]
    soma/=12
print(soma)

