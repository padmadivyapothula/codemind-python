a,b=map(int,input().split())
m=min(a,b)
while(m):
    if m%a==0 and m%b==0:
        print(m)
        break
    m+=1