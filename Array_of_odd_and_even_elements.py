n=int(input())
num=list(map(int,input().split()))
x=[]
for i in num:
    if i%2!=0:
        x.append(i)
for i in num:
    if i%2==0:
        x.append(i)
for j in x:
    print(j,end=" ")