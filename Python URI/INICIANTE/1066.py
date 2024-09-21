p = 0
po = 0
im = 0
ne = 0

for i in range(5):
    n = float(input())
    if n % 2 == 0:
        p+=1
    if n % 2 == 1 or n %  2 == -1:
        im+=1
    if n > 0:
        po+=1
    if n < 0:
        ne+=1

print(f'{p} valor(es) par(es)')
print(f'{im} valor(es) impar(es)')
print(f'{po} valor(es) positivo(s)')
print(f'{ne} valor(es) negativo(s)')