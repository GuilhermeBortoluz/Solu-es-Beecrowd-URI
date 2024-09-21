n1,n2,n3,n4 = map(float,input().split())
media = (n1*2 + n2*3 + n3*4 + n4*1)/10
print('Media: {:.1f}'.format(media))
if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    nota_ex = float(input())
    print(f'Nota do exame: {nota_ex:.1f}')
    media  = (media+nota_ex)/2
    if media >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {media:.1f}')

