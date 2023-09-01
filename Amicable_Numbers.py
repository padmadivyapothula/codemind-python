a=int(input())
b=int(input())
f=0
s=0
for i in range(1,a):
    if a%i==0:
        f=f+i
for i in range(1,b):
    if b%i==0:
        s=s+i
if f==b and s==a:
    print("Amicable")
else:
    print("Not Amicable")