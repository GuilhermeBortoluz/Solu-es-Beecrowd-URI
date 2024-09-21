x = int(input())
z = 0
cont = 0
soma = 0
while True:
    candidato_z = int(input())
    if candidato_z > x:
        z = candidato_z
        break

cont = 0
soma = 0
while soma < z:
    soma+=x
    cont+=1
    x+=1
    
print(cont)