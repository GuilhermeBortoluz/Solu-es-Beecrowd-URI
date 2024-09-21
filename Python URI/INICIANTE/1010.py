c_1, n_1, vu_1 = map(float, input().split()); int(c_1); int(n_1)
c_2, n_2, vu_2 = map(float, input().split()); int(c_2); int(n_2)

Total = n_1 * vu_1 + n_2*vu_2

print(f'VALOR A PAGAR: R$ {Total:.2f}')