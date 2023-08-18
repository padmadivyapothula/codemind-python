a,b,c=map(int,input().split())
d=b*c
e=a%d
if e==0:
    print(f"{a//d}")
else:
    print(f"{(a//d)+1}")