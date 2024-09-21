n = int(input())
lista = []
for i in range(n):
    v1,v2,v3 = map(float, input().split())
    media = (v1*2 + v2*3 + v3*5)/10
    media = round(media,1)
    lista.append(media)

for j in lista:
    print(j)
