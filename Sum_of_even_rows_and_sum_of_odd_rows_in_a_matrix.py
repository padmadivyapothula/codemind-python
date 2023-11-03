r,c=map(int,input().split())
s=0
o=0
mat=[]
for i in range(r):
    inner_list=list(map(int,input().split()))
    mat.append(inner_list)
for i in range(r):
    for j in range(c):
        if i%2==0:
             s+=mat[i][j]
        else:
            o+=mat[i][j]
print(f"{s} {o}")