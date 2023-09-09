a=int(input())
f=0
for i in range(1,a):
    b=i*(i+1)
    if b==a:
        f=1
        break
    else:
        f=0
if f==1:
    print("YES")
else:
    print("NO")