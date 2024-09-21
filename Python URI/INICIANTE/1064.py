contador =0
t = []
for x in range(1,7):
    v = float(input())
    if v > 0:
        contador += 1
        t.append(v)

media = (sum(t))/len(t)

print(f'{contador} valores positivos')
print(round(media,1))