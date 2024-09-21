lista = []
while True:
    x,y = map(int,input().split())

    
    if x == 0  or y == 0:
        break
    elif (x>0 and y>0):
        lista.append('primeiro')
    if x < 0 and y > 0:
        lista.append('segundo')
    elif (x < 0 and y < 0):
        lista.append('terceiro')
    elif x > 0 and y < 0:
        lista.append('quarto')
    
for i in lista:
    print(i)
