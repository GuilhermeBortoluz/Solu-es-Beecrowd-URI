h, hf = map(int,input().split())

if h < hf:
    hf -= h
else:
    hf = (24-h) + hf
print('O JOGO DUROU {} HORA(S)'.format(hf))


