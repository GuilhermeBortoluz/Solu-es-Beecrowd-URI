def primo(n):
    primo = [x for x in range(2,(n//2)+1) if n%x==0]
    if primo == []:return True
    else:return False

t = int(input())
for i in range(0,t):
    n = int(input())
    if (eh_primo:=primo(n))==True:print(f'{n} eh primo')
    else:print(f'{n} nao eh primo')