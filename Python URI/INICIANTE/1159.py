soma = 0
while True:
    if (x := int(input()))==0:break
    if x%2==0:soma=5*x + 20
    else:x+=1;  soma=5*x + 20
    print(soma)