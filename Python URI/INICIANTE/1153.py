def fatorial():
    n = int(input())
    n_inicial = n
    for i in range(1,n-1):n = n * (n_inicial-i);
    return n
print(fatorial())