vetor = []
i=0
while len(vetor) != 10:
    valor = int(input())
    vetor.append(valor)

for j in vetor:
    if j <= 0 : print(f'X[{i}] = 1')
    else:print(f'X[{i}] = {j}')
    i+=1
    