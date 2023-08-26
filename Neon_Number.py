a=int(input())
s=0
n=a*a
while(n>0):
    r=n%10
    s=s+r
    n=n//10
if s==a:
    print("Neon Number")
else:
    print("Not Neon Number")