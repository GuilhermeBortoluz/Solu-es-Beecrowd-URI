import os
os.system('cls')
tempo = int(input())
horas = tempo//3600
x = (tempo - (horas*3600))/60
min = int(x)
s = (x - min)*60
print(f"{horas}:{min}:{s:.0f}")
