s1,s2,s3,s4,s5=map(int,input().split())
ans=(s1+s2+s3+s4+s5)//5
if ans>=90:
    print("Grade A")
elif ans>=80:
    print("Grade B")
elif ans>=70:
    print("Grade C")
elif ans>=60:
    print("Grade D")
elif ans>=40:
    print("Grade E")    
else:
    print("Grade F")    