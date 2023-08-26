a=int(input())
s=0
b=a*(a+1)//2
c=b*b
for i in range(1,a+1):
    s=s+i*i
ans=c-s
print(ans)