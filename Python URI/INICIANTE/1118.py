def media(p):
    soma = 0
    for i in p:
        soma+=i 
    media = soma/len(p)
    return media

notas = []
x=1
while x==1:
    while len(notas)<2:
        nota = float(input())
        if 0<=nota<=10:notas.append(nota)
        else:print('nota invalida')

    
    print('media =',media(notas))
    
    while True:
        x = int(input('novo calculo (1-sim 2-nao)'))
        
        if x == 1:
            notas= []
            break
        elif x == 2:break 
    if x == 2:break
           