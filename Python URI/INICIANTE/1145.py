x, y = map(int,input().split())


for j in range(1, y + 1):
    print(j, end='')
    if j % x == 0:
        print('')
    else:
        print(' ', end='')

