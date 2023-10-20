n=int(input())
k=str(n)
d=len(k)
s=0
q=n
while n!=0:
    r=n%10
    s=s+(r**d)
    n=n//10
    d=d-1
if s==q:
    print("True")
else:
    print("False")