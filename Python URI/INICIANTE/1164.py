

def eh_perfeito(num):
    soma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            soma_divisores += i
    return soma_divisores == num
N= int(input())
# Exemplo de uso:
for _ in range(N):
    numero = int(input())
    if eh_perfeito(numero):
        print(numero, "eh perfeito.")
    else:
        print(numero, "nao eh perfeito.")