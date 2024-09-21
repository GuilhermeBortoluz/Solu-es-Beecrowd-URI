v1 = float(input())
v2 = float(input())
v3 = float(input())
v4 = float(input())
v5 = float(input())
v6 = float(input())
p =0
lista = [v1,v2,v3,v4,v5,v6]

for x in lista:
    if x < 0:
        p+=1

print(f'{p} valores positivos')
        

