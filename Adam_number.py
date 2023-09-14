n=int(input())
s=0
se=0
sq=n*n
q=n
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
squ=s*s
while squ!=0:
    r=squ%10
    se=se*10+r
    squ=squ//10
if se==sq:
    print("True")
else:
    print("False")
    