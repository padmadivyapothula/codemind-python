n=int(input())
num=list(map(int,input().split()))
o=0
e=0
for i in num:
    if i%2!=0:
        o+=i
for i in num:
    if i%2==0:
        e+=i
s=abs(e-o)
print(s)