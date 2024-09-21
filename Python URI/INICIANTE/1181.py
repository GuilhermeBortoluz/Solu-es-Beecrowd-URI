matriz = []
for i in range(0,12):
    matriz.append([])
    for _ in range(0,12):
        matriz[i].append(0)

linha = int(input())
opr = input()

for i in range(0,12):
    for j in range(0,12):
        matriz[i][j] = float(input())


soma = 0

if opr =='S':
    for i in range(0,12):
        soma += matriz[linha][i]

if opr == 'M':
    for i in range(0,12):
        soma += matriz[linha][i]
    soma/=12
print(soma)