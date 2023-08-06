s = int(input())
h=s//3600
se=s-(h*3600)
m=se//60
secs=se%60
print(f"H:M:S-{h}:{m}:{secs}")