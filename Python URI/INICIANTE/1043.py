a,b,c = map(float,input().split())

numero = [a,b,c]
numero = sorted(numero)

if (numero[0] + numero[1]) > numero[2]:
    soma = sum(numero)
    print(f'Perimetro = {soma:.1f}')
else:
    area = ((a+b)*c)/2
    print(f'Area = {area:.1f}')
