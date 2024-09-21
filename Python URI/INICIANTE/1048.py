sal = float(input())
if sal >= 0 and sal <= 400:
    per = 15
    reaj = sal * (per/100)
elif sal >= 400.01 and sal <= 800:
    per = 12
    reaj = sal * ( per/100)

elif sal >= 800.01 and sal <= 1200:
    per = 10
    reaj = sal * (per/100)
elif sal >= 1200.01 and sal <= 2000:
    per = 7
    reaj = sal * (per/100)
elif sal > 2000:
    per = 4
    reaj = sal * (per/100)
sal = reaj + sal
print(f"Novo salario: {sal:.2f}")
print(f'Reajuste ganho: {reaj:.2f}')
print('Em percentual:',per,'%')
