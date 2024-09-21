
quant_grenais = 0
vit_gremio = 0
vit_inter = 0
empates = 0
gols_gremio = 0
gols_inter = 0
opc  = 1
while opc == 1:
    
    gols_inter,gols_gremio  = map(int, input().split())
    if gols_gremio>gols_inter:
        vit_gremio+=1
    elif gols_gremio<gols_inter:
        vit_inter+=1
    else:
        empates+=1
    quant_grenais+=1
    opc = int(input('Novo grenal (1-sim 2-nao)'))
    if opc == 2:
        break

print(f'{quant_grenais:.0f} grenais')
print(f'Inter: {vit_inter:.0f}')
print(f'Gremio: {vit_gremio:.0f}')
print(f'Empates: {empates:.0f}')
if vit_gremio<vit_inter:print('Inter venceu mais')
elif vit_gremio>vit_inter:print('Gremio venceu mais')
else:print('Não houve vencedor')