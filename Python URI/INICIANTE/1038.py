c, q = map(int, input().split())
codigo = {1:4, 2:4.5, 3:5,4:2,5:1.5}
p = q * codigo[c]
print(f'Total: R$ {p:.2f}')
