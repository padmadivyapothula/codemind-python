n=int(input())
num=list(map(int,input().split()))
e=[]
for i in num:
    if i%2==0:
        e.append(i)
for i in num:
    if i%2!=0:
        e.append(i)
for j in e:
    print(j,end=' ')