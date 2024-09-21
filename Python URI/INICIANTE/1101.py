lista = []
while True:
    m, n = map(int,input().split())
    if n <= 0 or m <= 0:
        break
    if n < m:
        m, n = n, m
    vetor = [i for i in range(m,n+1)]
    
    lista.append(vetor)
for sublista in lista:
    print(*sublista,'Sum='+str(sum(sublista)))
