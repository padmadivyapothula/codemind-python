u=int(input())
if u<=199:
    c=1.20
elif u>=200 and u<400:
    c=1.40
elif u>=400 and u<600:
    c=1.60
elif u>=600 and u<800:
    c=1.80
elif u>=800:
    c=2.00
b= u*c
if b>400:
    s=b*0.15
else:
    s=0
bill=b+s
print(f"Units Consumed: {u}",sep="
")
print(f"Cost per Unit: {c:.2f}",sep="
")
print(f"Bill: {b:.2f}",sep="
")
print(f"Surcharge: {s:.2f}",sep="
")
print(f"Total Amount: {bill:.2f}")
