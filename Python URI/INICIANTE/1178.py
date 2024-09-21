x = float(input())
v = [x]

for i in range(99):
    t = x/2
    x = t
    v.append(x)
c=0
for i in v:
    print(f'N[{c}] = {i:.4f}')
    c+=1

