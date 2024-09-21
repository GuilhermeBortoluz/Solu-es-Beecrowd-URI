n = int(input())
cont = 0
total = 0
c = 0
r = 0
s = 0

for i in range(n):
    n, animal = input().split()
    n = int(n)
    total += n
    if animal == 'C':
        c += n
    if animal == 'R':
        r += n
    if animal == 'S':
        s+= n



pc = c*100/total
pr = r*100/total
ps = s*100/total
    
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')
print(f'Percentual de coelhos: {pc:.2f} %')
print(f'Percentual de ratos: {pr:.2f} %')
print(f'Percentual de sapos: {ps:.2f} %')
