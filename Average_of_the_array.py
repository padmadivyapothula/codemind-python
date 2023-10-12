n=int(input())
num=list(map(int,input().split()))
s=0
for i in num:
    s+=i
avg=s/n
print(f'{avg:.2f}')