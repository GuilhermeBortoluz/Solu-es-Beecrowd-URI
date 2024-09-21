lista = a,b,c = list(map(float, input().split()))
lista1 = lista
lista.sort(key= float,reverse=True)

a = lista[0]; b = lista[1]; c = lista[2]


    

if a >= b + c:
    print("NAO FORMA TRIANGULO")

elif (a**2) == (b**2 + c**2): 
    print("TRIANGULO RETANGULO")
elif (a**2) > (b**2+ c**2):
    print("TRIANGULO OBTUSANGULO")
elif (a**2) < (b**2 + c**2):
    print('TRIANGULO ACUTANGULO')



if a == b and b == c:
    print("TRIANGULO EQUILATERO")
elif (a == b and b != c) or (b == c and c != a) or (a == c and c != b):
    print('TRIANGULO ISOSCELES')
