a=int(input())
b=a%4
if b==0:
    print(f"{a//4}")
else:
    print(f"{(a//4)+1}")