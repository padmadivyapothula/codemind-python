n=int(input())
num=list(map(int,input().split()))
l=[]
for i in num:
    if i not in l:
        l.append(i)
for j in l:
    print(j,end=' ')