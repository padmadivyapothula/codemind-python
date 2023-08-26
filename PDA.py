a=int(input())
s=0
for i in range(1,a):
    if a%i==0:
        s=s+i
if s==a:
    print("PERFECT")
elif s<a:
    print("DEFICIENT")
else:
    print("ABUNDANT")