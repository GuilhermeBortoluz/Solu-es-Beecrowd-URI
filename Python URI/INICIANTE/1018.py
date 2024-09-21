#entrada

valor = int(input())
valor2 = valor
cem = 0; cinq = 0; vin = 0; dez = 0; cinc = 0; dois = 0; um= 0
#processamento


while valor >= 100:
    cem += 1
    valor -= 100
    

while valor >= 50:
    cinq += 1
    valor -= 50

while valor >= 20:
    vin += 1
    valor -= 20
while valor >= 10:
    dez += 1
    valor-=10
while valor >= 5:
    cinc +=1
    valor-=5
while valor >= 2:
    dois +=1
    valor-=2
while valor >= 1:
    um+=1
    valor-=1

#Saída:
print(f'{valor2}\n{cem} nota(s) de R$ 100,00\n{cinq} nota(s) de R$ 50,00\n{vin} nota(s) de R$ 20,00\n{dez} nota(s) de R$ 10,00\n{cinc} nota(s) de R$ 5,00\n{dois} nota(s) de R$ 2,00\n{um} nota(s) de R$ 1,00')
   