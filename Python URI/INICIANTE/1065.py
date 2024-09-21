p = 0

for i in range(1,6):
    n = float(input())
    if n % 2 == 0:
        p+=1

print(f'{p} valores pares')