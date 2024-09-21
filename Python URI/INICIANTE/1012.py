a, b, c = map(float, input().split())
PI = 3.14159
a_tri = (a*c)/2
a_cir = c**2 * PI 
a_trap = ((a+b)*c)/2
a_quad = b**2
a_retan = a*b

print(f'TRIANGULO: {a_tri:.3f}\nCIRCULO: {a_cir:.3f}\nTRAPEZIO: {a_trap:.3f}\nQUADRADO: {a_quad:.3f}\nRETANGULO: {a_retan:.3f}')