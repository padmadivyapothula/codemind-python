n=int(input())
q=n
s=0
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
if s==q:
    print("True")
else:
    print("False")