m = []
def menu():
    opr = input()
    return opr

def matriz():
    for i in range(0,12):
        m.append([])
        for _ in range(0,12):
            m[i].append(0)
    return m

def fill_matriz(m):
    for i in range(0,12):
        for j in range(0,12):
            m[i][j]= float(input())
    return m

def sum_matriz(m):
    soma=0
    for i in range(0,12):
        for j in range(0,12):
            if j>i:soma+=m[i][j]
    return soma
def median_matriz(m):
    soma = sum_matriz(m)
    count = 12 * (12 - 1) // 2  # 66 elementos acima da diagonal principal
    return soma / count


matriz()
opr=menu()
fill_matriz(m)
if opr == 's':
    print(sum_matriz(m))
if opr == 'm':
    print(median_matriz(m))




