r,c=map(int,input().split())
mat=[]
s=0
for i in range(r):
    inner_value=list(map(int,input().split()))
    mat.append(inner_value)
for inner_value in mat:
    for every_value in inner_value:
        s+=every_value
print(s)