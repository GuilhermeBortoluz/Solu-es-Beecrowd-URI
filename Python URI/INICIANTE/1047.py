import os
os.system('cls')
h, m, hf, mf= map(int,input().split())
tempo =0

if hf > h:
    if mf >= m:
        h = hf - h
        m = mf - m
    else:
        hf_m = (hf * 60) + mf
        h_m = (h * 60) + m
        total_m = hf_m-h_m
        total_h = int(total_m/60)
        total_m = ((total_m/60) - (total_h))*60
        h = total_h
        m = round(total_m)

elif hf == h and mf == m:
    h = 24
    m = 0
elif hf == h and mf > m:
    h = 0
    m = mf - m
        
elif hf <= h:
    hf_m = (hf * 60) + mf #20
    h_m = (h * 60) + m #30
    z = 1440 - h_m #1410
    total_m = z + hf_m# 1430
    total_h = int(total_m/60)#23
    total_m = ((total_m/60) - (total_h))*60# 50
    h = total_h 
    m = round(total_m)




print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')

        

        








