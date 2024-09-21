v = []
t = int(input())
for i in range(1000):
    v.append(i%t)
j = 0
for i in v:
    print(f'N[{j}] = {i}')
    j+=1
 