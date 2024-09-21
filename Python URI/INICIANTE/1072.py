n = int(input())
cont = 0
dentro = 0
fora = 0


while n != cont:
    x = int(input())
    if 10<=x<=20:
        dentro += 1
    else:
        fora += 1
    cont +=1
print(f'{dentro} in')
print(f'{fora} out')