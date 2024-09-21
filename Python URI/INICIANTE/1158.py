n = int(input())
soma=0
for i in range(1,n+1):
    x,y = map(int,input().split())
    if x%2==0:#par
        x+=1
        soma = (y*x) + ((y**2)-y)
    else:#impar
        soma = (y*x) + ((y**2)-y)
        
    print(soma)

        
    
    
    
    
        