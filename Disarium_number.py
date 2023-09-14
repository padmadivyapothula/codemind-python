n=int(input())
s=0
c=0
y=0
q=n
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
while s>0:
    r=s%10
    c=c+1
    x=r**c
    y=x+y
    s=s//10
if y==q:
    print("True")
else:
    print("False")
    