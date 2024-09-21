from math import gcd
X = int(input())
for i in range(X):
    x, y = map(int,input().split())
    print(gcd(x,y))
