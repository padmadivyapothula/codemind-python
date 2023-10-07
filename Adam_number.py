n=int(input())
sq=n*n
s=0
s1=0
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
sq1=s*s
while sq1!=0:
    r1=sq1%10
    s1=s1*10+r1
    sq1=sq1//10
if s1==sq:
    print("True")
else:
    print("False")