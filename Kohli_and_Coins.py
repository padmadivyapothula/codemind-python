a=int(input())
b=a%10
c=a%5
if b==0:
    print(f"{a//10}")
elif c == 0:
    print(f"{(a//10)+1}")
else:
    print("-1")
