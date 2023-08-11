a,b,c=map(int,input().split())
s=(a+b+c)/2
ar=(s*(s-a)*(s-b)*(s-c))
ans=(ar**0.5)
print(f"{ans:.2f}")
