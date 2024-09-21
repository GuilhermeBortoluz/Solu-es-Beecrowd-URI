vp = []
vi = []
for i in range(15):
    x = int(input())
    if x %2 == 0:vp.append(x)
    else:vi.append(x)
    if( (len(vp)) == 5):
        c=0
        for i in vp:
            print(f'par[{c}] = {i}')
            c+=1
        vp.clear()
        
    if ((len(vi)) == 5):
        c=0
        for i in vi:
            print(f'impar[{c}] = {i}')
            c+=1
        vi.clear()
        


if (len(vi)> 0):
    c=0
    for i in vi:
        print(f'impar[{c}] = {i}')
        c+=1
if (len(vp)> 0):
    c= 0
    for i in vp:
        print(f'par[{c}] = {i}')
        c+=1