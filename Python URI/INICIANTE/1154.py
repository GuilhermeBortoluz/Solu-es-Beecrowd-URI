array = []
while True:
    if (idade:=int(input()))>=0:array.append(idade)
    else:break
print(f'{sum(array)/len(array):.2f}')