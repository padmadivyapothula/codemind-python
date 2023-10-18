n=int(input())
num=list(map(int,input().split()))
a,b=map(int,input().split())
n=sum(num)
s=0
for i in num:
    if i>=a and i<=b:
        s=s+i
print(n-s)