
x = int(input())
y = int(input())
if x > y: 
    x, y = y, x
def rest_divisao(x,y):
    for j in range(x+1,y):
        if j % 5 == 2 or j % 5 == 3:print(j)
        
rest_divisao(x,y)