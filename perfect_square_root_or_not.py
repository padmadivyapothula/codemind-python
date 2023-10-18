n=int(input())
f=False
for i in range(1,n):
    if i*i==n:
        f=True
        break
if f==True:
    print("True")
else:
    print("False")