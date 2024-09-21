t =int(input())
for i in range(t):
    valores = input().split()
    Pa = int(valores[0])
    Pb = int(valores[1])
    Ca = float(valores[2])/100
    Cb = float(valores[3])/100
    anos = 0
    while True: 
        Pa += int(Pa*Ca);Pb += int(Pb*Cb)  
        anos+=1    
        if anos >100 or Pa>Pb:break

    if anos <= 100:print(f'{anos} anos.')
    else:print('Mais de 1 seculo.')