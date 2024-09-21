numeros= input().split()
a = int(numeros[0])
n = int(numeros[len(numeros)-1])
soma = 0
for i in range(0,n):
    soma+=i + a   
print(soma)