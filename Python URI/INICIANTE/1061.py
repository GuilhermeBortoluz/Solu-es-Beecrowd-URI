dia = int(input().split()[1])
h,m,s = map(int, input().split(':'))

t1 = s + m * 60 + h*60*60 + dia*24*60*60


diaf = int(input().split()[1])
hf,mf,sf = map(int, input().split(':'))

t2 = sf + mf *60 + hf*60*60 + diaf*24*60*60

dif = t2 - t1

d = dif //( 24 * 60*60)
dif  = dif %( 24 * 60*60)

h = dif //( 60*60)
dif = dif %( 60*60)

m = dif // 60
dif = dif%60

s = dif

print(f'{d} dia(s)')
print(f'{h} hora(s)')
print(f'{m} minuto(s)')
print(f'{s} segundo(s)')

