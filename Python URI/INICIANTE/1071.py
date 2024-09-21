x = int(input())
y = int(input())
n = 0

if x > y:
    for i in range(y+1,x):
        if i % 2 != 0 or i % 2 < 0:
            n += i
    

elif x < y :
    x = y
    y = x
    for i in range(y+1, x):
        if i % 2 !=0 or i % 2 < 0:
            n += i

print(n)