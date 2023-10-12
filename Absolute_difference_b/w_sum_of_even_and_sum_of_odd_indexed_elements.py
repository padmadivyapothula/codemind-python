n=int(input())
num=list(map(int,input().split()))
e=0
o=0
for i in range(len(num)):
    if i%2==0:
        e+=num[i]
for i in range(len(num)):
    if i%2!=0:
        o+=num[i]
s=abs(e-o)
print(s)