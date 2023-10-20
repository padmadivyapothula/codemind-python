n=int(input())
num=list(map(int,input().split()))
s=0
c=0
for i in num:
    s+=i
x=s//n
for i in num:
    if i>=x:
        c+=1
print(c)
    