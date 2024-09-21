import os
os.system('cls')
tempo = int(input())
ano = tempo//365
y = (tempo-(ano*365))
mes = y//30
dias = y - (mes*30)
print(f'{ano} ano(s)\n{mes} mes(es)\n{dias} dia(s)')
