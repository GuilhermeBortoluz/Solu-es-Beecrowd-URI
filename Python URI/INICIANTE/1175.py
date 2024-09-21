array = []
for i in range(20):
    e = int(input())
    array.append(e)
p = -1
pi = 0
intermedio = 0
f = 0
for j in range(0,10):
    intermedio = array[pi]
    array[pi]= array[p]
    array[p]= intermedio
    p-=1
    pi+=1
pos = 0
for t in array:
    print(f'N[{pos}] = {t}')
    pos+=1



