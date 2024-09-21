a, b, c = map(int,input().split())

maiorab = (a+b+abs(a-b))/2
maiorc = (maiorab+c+abs(maiorab-c))/2

print(f'{maiorc:.0f} eh o maior')
