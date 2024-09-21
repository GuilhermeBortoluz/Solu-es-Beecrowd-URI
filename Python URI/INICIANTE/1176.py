fibo = [0,1]
inicio = 0
fim =1

for i in range(60):
    sequencia = inicio+fim
    fibo.append(sequencia)
    inicio = fim
    fim = sequencia

N = int(input())
for m in range(0,N):
    x = int(input())
    print(f'Fib({x}) = {fibo[x]}')