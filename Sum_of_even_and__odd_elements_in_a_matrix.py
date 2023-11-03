r,c=map(int,input().split())
mat = []
s=0
o=0
for i in range(r):
    inner_list = list(map(int,input().split())) [:c:]
    mat.append(inner_list)
for inner_list in mat:
    for every_value in inner_list:
        if every_value%2==0:
            s=s+every_value
        else:
            o+=every_value
print(f"{s} {o}")
            