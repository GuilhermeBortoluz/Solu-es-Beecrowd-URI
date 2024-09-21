n = int(input())
a = 0
q = 2
pg = [n]
while len(pg) != 10:
    n = pg[a]*q
    pg.append(n)
    a+=1
pos = 0
for i in pg:
    print(f'N[{pos}] = {i}')
    pos+=1