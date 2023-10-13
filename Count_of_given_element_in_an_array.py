n=int(input())
num=list(map(int,input().split()))
z=int(input())
c=0
for i in num:
    if z==i:
        c+=1
print(c)